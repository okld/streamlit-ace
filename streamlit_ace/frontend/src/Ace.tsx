import React, { useEffect, useRef } from "react"
import AceEditor from "react-ace"
import { IAceEditor } from "react-ace/lib/types"
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "./streamlit"

import "ace-builds/webpack-resolver"
import "ace-builds/src-min-noconflict/ext-emmet"
import "ace-builds/src-min-noconflict/ext-language_tools"

interface AceProps extends ComponentProps {
  args: any
}

const Ace = ({ args }: AceProps) => {
  const pendingRef = useRef<HTMLDivElement>(null)

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
    if (args.autoUpdate) {
      updateStreamlit(value)      
    }
    else {
      showPending(true)
    }
  }
  
  // Update component height with an offset for the pending message
  useEffect(() => {
    Streamlit.setFrameHeight(args.height + 20)
  })

  // Set default prop values that shouldn't be exposed to python
  args.enableBasicAutocompletion = true
  args.enableLiveAutocompletion = true
  args.debounceChangePeriod = 100
  args.onChange = handleChange
  args.width = "100%"
  args.commands = [{
    name: "updateStreamlit",
    bindKey: { mac: "Command-Enter", win: "Ctrl-Enter" },
    exec: (editor: IAceEditor) => {
      if (isPending()) {
        updateStreamlit(editor.getValue())
      }
    }
  }]

  return <>
    <AceEditor {...args} />
    <div
      ref={pendingRef}
      style={{
        textAlign: "right",
        fontSize: ".8rem",
        color: "#a3a8b8",
        display: "none"
      }}
    >
      Press Ctrl+Enter to apply
    </div>
  </>
}

export default withStreamlitConnection(Ace)
