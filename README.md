# Streamlit Ace [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/okld/streamlit-ace/demo/)

[Ace editor](https://ace.c9.io/) component for [Streamlit](https://www.streamlit.io/).

Implemented with [React ace](https://github.com/securingsincity/react-ace).

## Getting started 

### Installation

```sh
pip install streamlit-ace
```

### Quick usage

```python
import streamlit as st
from streamlit_ace import st_ace

# Spawn a new Ace editor
content = st_ace()

# Display editor's content as you type
content
```

## Demo

You can access the demo app [here](https://share.streamlit.io/okld/streamlit-ace/demo/), and its source code [there](https://github.com/okld/streamlit-ace/blob/master/demo/streamlit_app.py).

[![Demo Image](https://raw.githubusercontent.com/okld/streamlit-ace/master/demo/streamlit_ace_demo.gif)](https://share.streamlit.io/okld/streamlit-ace/demo/)
