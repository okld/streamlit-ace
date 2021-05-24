import streamlit as st

from pathlib import Path
from streamlit.components.v1.components import declare_component
from streamlit_ace.version import __release__, __version__

if __release__:
    _source = {"path": (Path(__file__).parent/"frontend"/"build").resolve()}
else:
    _source = {"url": "http://localhost:3001"}

_render_component = declare_component("streamlit_ace", **_source)

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/mode-*.js
LANGUAGES = [
    "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", 
    "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru", 
    "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", 
    "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", 
    "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", 
    "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", 
    "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", 
    "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", 
    "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", 
    "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode", 
    "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6", 
    "pgsql", "php", "php_laravel_blade", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", 
    "properties", "protobuf", "puppet", "python", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml", 
    "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty", 
    "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", 
    "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", 
    "velocity", "verilog", "vhdl", "visualforce", "wollok", "xml", "xquery", "yaml"
]

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/theme-*.js
THEMES = [
    "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
    "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
    "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
    "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
    "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
    "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
]

# Source: https://github.com/ajaxorg/ace-builds/tree/master/src/keybinding-*.js
KEYBINDINGS = [
    "emacs", "sublime", "vim", "vscode"
]


def st_ace(
    value="",
    placeholder="",
    height=None,
    language="plain_text",
    theme="chrome",
    keybinding="vscode",
    min_lines=12,
    max_lines=None,
    font_size=14,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=False,
    readonly=False,
    annotations=None,
    markers=None,
    auto_update=False,
    key=None
):
    """Display an Ace editor.

    Parameters
    ----------
    value : any
        The text value of this widget when it first renders.
        Empty string by default.
    placeholder : any
        The text value of this widget when the editor is empty.
        Empty string by default.
    height : int or None
        Desired height of the UI element expressed in pixels.
        If set to None, height will auto adjust to editor's content.
        None by default.
    language : str or None
        Language for parsing and code highlighting. If None, the editor
        will not highlight content.
        Available languages are defined in streamlit_ace.LANGUAGES.
        Plain text by default.
    theme : str or None
        The theme to use. If None, a default theme is used.
        Available themes are defined in streamlit_ace.THEMES.
        Chrome by default.
    keybinding : str
        Keybinding mode set.
        Available keybindings are defined in streamlit_ace.KEYBINDINGS.
        Vscode by default.
    min_lines : int or None
        Minimum number of lines allowed in editor. 12 by default.
    max_lines : int or None
        Maximum number of lines allowed in editor. None by default.
    font_size : int or None
        The font size of the enditor. 14 by default.
    tab_size : int or None
        The size of a tabulation. 4 by default.
    show_gutter : bool
        Show or hide gutter. True by default.
    show_print_margin : bool
        Show or hide print margin. False by default
    wrap : bool
        Enable line wrapping. False by default.
    readonly : bool
        Make the editor read only. False by default.
    annotations : list or None
        Anootations to show in the editor. None by default.
    markers : list or None
        Markers to show in the editor. None by default.
    auto_update : bool
        Choose whether Streamlit auto updates on input change, or waits
        for user validation. False by default.
    key : str
        An optional string to use as the unique key for the widget.
        If this is omitted, a key will be generated for the widget
        based on its content. Multiple widgets of the same type may
        not share the same key.
    
    Returns
    -------
    str
        The current content of the ace editor widget.
    """
    return _render_component(
        defaultValue=str(value),
        placeholder=str(placeholder),
        height=height,
        minLines=min_lines,
        maxLines=max_lines,
        fontSize=font_size,
        tabSize=tab_size,
        mode=language,
        theme=theme,
        showGutter=show_gutter,
        showPrintMargin=show_print_margin,
        wrapEnabled=wrap,
        readOnly=readonly,
        keyboardHandler=keybinding,
        annotations=annotations or [],
        markers=markers or [],
        autoUpdate=auto_update,
        key=key,
        default=str(value),
    )
