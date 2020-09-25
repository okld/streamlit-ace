import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { useEffect, useRef } from "react"
import AceEditor from "react-ace"
import { IAceEditor } from "react-ace/lib/types"

import "ace-builds/webpack-resolver"
import "ace-builds/src-min-noconflict/ext-emmet"
import "ace-builds/src-min-noconflict/ext-language_tools"

interface AceProps extends ComponentProps {
  args: any
}

const Ace = ({ args }: AceProps) => {
  const pendingRef = useRef<HTMLDivElement>(null)
  const editorRef = useRef<IAceEditor>(null)
  const debounceRef = useRef<number>(0)
  let timeout: NodeJS.Timeout

  const isPending = () => pendingRef.current?.style.display === "block"

  const showPending = (display: boolean) => {
    if (pendingRef.current) {
      pendingRef.current.style.display = display ? "block" : "none"
    }
  }

  // Send editor content to streamlit
  const updateStreamlit = (value: string) => {
    Streamlit.setComponentValue(value)
    showPending(false)
  }

  // Called on editor update
  const handleChange = (value: string) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      if (args.autoUpdate) {
        updateStreamlit(value)      
      }
      else {
        showPending(true)
      }
    }, debounceRef.current)
  }
  
  // Update component height with an offset for the pending message
  useEffect(() => {
    Streamlit.setFrameHeight(args.height + 20)

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
          else if (isPending()) {
            updateStreamlit(editor.getValue())
          }
        }
      })

      debounceRef.current = args.autoUpdate ? 200 : 0
    }
  })

  // Set default prop values that shouldn't be exposed to python
  args.enableBasicAutocompletion = true
  args.enableLiveAutocompletion = true
  args.onChange = handleChange
  args.width = "100%"

  return <>
    <AceEditor ref={editorRef} {...args} />
    <div
      ref={pendingRef}
      style={{
        color: "#a3a8b8",
        display: "none",
        fontSize: ".8rem",
        textAlign: "right",
      }}
    >
      Press {editorRef.current?.editor.commands.platform === "mac" ? "Cmd" : "Ctrl"}+Enter to apply
    </div>
  </>
}

export default withStreamlitConnection(Ace)
