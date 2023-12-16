import { useEffect, useRef, useState } from "react"
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
  Theme,
} from "streamlit-component-lib"
import AceEditor from "react-ace"
import { IAceEditor } from "react-ace/lib/types"
import { Paper, Button, Grid } from "@material-ui/core"
import { MuiThemeProvider, createTheme } from "@material-ui/core/styles"

import "ace-builds/webpack-resolver"
import "ace-builds/src-min-noconflict/ext-emmet"
import "ace-builds/src-min-noconflict/ext-language_tools"

interface AceProps extends ComponentProps {
  args: any
  theme?: Theme
}

const Ace = ({ args, theme }: AceProps) => {
  const [colors, setColors] = useState<any>({})
  const [changed, setChanged] = useState<boolean>(false)
  const editorRef = useRef<IAceEditor>(null)
  const debounceRef = useRef<number>(0)

  let timeout: NodeJS.Timeout

  // Send editor content to streamlit
  const updateStreamlit = (value: string) => {
    Streamlit.setComponentValue(value)
    setChanged(false)
  }

  // Called on editor update
  const handleChange = (value: string) => {
    clearTimeout(timeout)

    timeout = setTimeout(() => {
      if (args.autoUpdate) {
        updateStreamlit(value)
      }
      else {
        setChanged(true)
      }
    }, debounceRef.current)
  }

  // Update content keybinding
  useEffect(() => {
    if (editorRef.current) {
      const editor = editorRef.current.editor

      editor.commands.removeCommand("addLineAfter")
      editor.commands.addCommand({
        name: "updateStreamlit",
        bindKey: {mac: "cmd-return", win: "ctrl-return"},
        exec: (editor: IAceEditor) => {
          if (args.autoUpdate) {
            editor.selection.clearSelection();
            editor.navigateLineEnd();
            editor.insert("\n");
          }
          else if (changed) {
            updateStreamlit(editor.getValue())
          }
        }
      })

      debounceRef.current = args.autoUpdate ? 200 : 0
    }
  })

  // Update theme
  useEffect(() => {
    setColors({
      palette: {
        primary: {
          main: theme?.primaryColor,
          background: {
            default: theme?.backgroundColor,
          },
          text: {
            primary: theme?.textColor,
          }
        }
      }
    })
  }, [theme?.primaryColor, theme?.backgroundColor, theme?.textColor])


  // Set default prop values that shouldn't be exposed to python
  args.onChange = handleChange
  args.width = "100%"

  // Auto height
  if (!args.height) {
    args.maxLines = Infinity
  }

  const resizeObserver = new ResizeObserver((entries: any) => {
    Streamlit.setFrameHeight(entries[0].contentRect.height + 15)
  })

  const observeElement = (element: HTMLDivElement | null) => {
    if (element !== null)
      resizeObserver.observe(element)
    else
      resizeObserver.disconnect()
  }

  return (
    <div ref={observeElement}>
      <MuiThemeProvider theme={createTheme(colors)}>
        <Paper>
          <AceEditor ref={editorRef} {...args} />
        </Paper>
        { args.autoUpdate ? null :
          <Grid container justifyContent="flex-end">
            <Button
              variant="contained"
              color="primary"
              disabled={!changed}
              style={{ marginTop: 10 }}
              onClick={() => updateStreamlit(editorRef.current?.editor.getValue())}
            >
              Apply ({editorRef.current?.editor.commands.platform === "mac" ? "Cmd" : "Ctrl"}+Enter)
            </Button>
          </Grid>
        }
      </MuiThemeProvider>
    </div>
  )
}

export default withStreamlitConnection(Ace)
