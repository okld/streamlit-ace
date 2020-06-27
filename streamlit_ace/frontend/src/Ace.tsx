import React, { useEffect, useState } from "react"
import AceEditor from "react-ace"
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
  const [content, setContent] = useState<string>(args.defaultValue)

  // Set default prop values that shouldn't be exposed to python
  args.enableBasicAutocompletion = true
  args.enableLiveAutocompletion = true
  args.debounceChangePeriod = 200
  args.width = "100%"
   
  useEffect(() => {
    Streamlit.setFrameHeight(args.height)
  })

  const handleChange = (value: string) => {
    Streamlit.setComponentValue(value)
    setContent(value)
  }

  return <AceEditor value={content} onChange={handleChange} {...args} />
}

export default withStreamlitConnection(Ace)
