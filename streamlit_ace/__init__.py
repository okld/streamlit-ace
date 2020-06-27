import os
import streamlit as st
from collections import namedtuple

_RELEASE = True

if not _RELEASE:
    _ace = st.declare_component("ace", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _ace = st.declare_component("ace", path=build_dir)


def ace(
    value="",
    placeholder="",
    height=500,
    language="plain_text",
    theme="chrome",
    keybinding="vscode",
    min_lines=None,
    max_lines=None,
    font_size=12,
    tab_size=4,
    wrap=False,
    show_gutter=True,
    show_print_margin=False,
    readonly=False,
    annotations=[],
    markers=[],
    key=None
):
    """Display an Ace editor.

    This component relies internally on React-Ace. 
    
    You can find the list of available keybindings, languages and themes here:
    https://github.com/ajaxorg/ace-builds/tree/2ea299a2bee97fdf58fc90cb76eec6c45535a63f/src

    - keybinding-[keybinding].js
    - mode-[language].js
    - theme-[theme].js

    If you want to display a new instance of Ace, you need to set a custom
    key value.

    Parameters
    ----------
    value : any
        The text value of this widget when it first renders. This will be
        cast to str internally.
    placeholder: any
        The text value of this widget when the editor is empty. It will be
        cast to str internally.
    height : int or None
        Desired height of the UI element expressed in pixels. If None, a
        default height is used.
    language : str or None
        Language for parsing and code highlighting. If None, the editor
        will not highlight content.
    keybinding : str
        Keybinding mode set.
    theme : str or None
        The theme to use. If None, a default theme is used.
    min_lines : int or None
        Minimum number of lines allowed in editor.
    max_lines : int or None
        Maximum number of lines allowed in editor.
    font_size : int or None
        The font size of the enditor. If None, a default size is used.
    tab_size : int or None
        The size of a tabulation. If None, a default value is used.
    show_gutter : bool
        Show or hide gutter. If None, a default value is used.
    show_print_margin : bool
        Show or hide print margin. If None, a default value is used.
    wrap : bool
        Enable line wrapping. If None, a default value is used.
    readonly : bool
        Make the editor read only.
    annotation : list or None
        Anootations to show in the editor.
    markers : list or None
        Markers to show in the editor.
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
    return _ace(
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
        annotations=annotations,
        markers=markers,
        name=key or "ace-editor",
        key=key or "ace-editor"
    )


if not _RELEASE:
    st.sidebar.title("Ace editor")
    event = ace(
        placeholder=st.sidebar.text_input("Editor placeholder.", value="Some placeholder."),
        language=st.sidebar.selectbox("Language mode.", options=[
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
        ]),
        theme=st.sidebar.selectbox("Theme.", options=[
            "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
            "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
            "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
            "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
            "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
            "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
        ]),
        keybinding=st.sidebar.selectbox("Keybinding mode.", options=[
            "emacs", "sublime", "vim", "vscode"
        ]),
        font_size=st.sidebar.slider("Font size.", 5, 24, 12),
        tab_size=st.sidebar.slider("Tab size.", 1, 8, 4),
        show_gutter=st.sidebar.checkbox("Show gutter.", value=True),
        show_print_margin=st.sidebar.checkbox("Show print margin.", value=True),
        wrap=st.sidebar.checkbox("Wrap enabled.", value=False),
        readonly=st.sidebar.checkbox("Read-only.", value=False, key="ace-editor"),
    )

    st.write(event)

