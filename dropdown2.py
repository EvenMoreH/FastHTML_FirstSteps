from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Titled, Link, Meta, Script, Redirect
)

# for Docker
# app, rt = fast_app(static_path="static") # type: ignore

# for local
app, rt = fast_app(static_path="app/static") # type: ignore

# TODO:
#   1. Built options A to C in a way that when clicked:
#       1.1 Options menu closes
#       1.2 Dropdown button text changes to selected option

@rt("/")
def homepage():
    return Html(
        Head(
            Title("Fast Tools Hub"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org"),
            Link(rel="stylesheet", href="styles.css"),
            Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Div(
                Button(
                    "Dropdown",
                    hx_get="/show",
                    hx_target="#target",
                    style="width: max(200px, 20%)",
                ),
            ),
            Div(
                id="target",
                style="display: flex; flex-direction: column;"
            ),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF MY CONTENT WILL MOVE"),
        )
    )

@rt("/show")
def show():
    return Div(
                A("A"),
                A("B"),
                A("C"),
                id="target",
                style="display: flex; flex-direction: column; text-align: center; background: grey; width: max(200px, 20%); position: absolute;",
                # mouseleave trigger to hide content when mouse moves out of list of dropdown items
                hx_trigger="mouseleave delay:250ms",
                hx_get="/hide",
            )

@rt("/hide")
def hide():
    return Div(
                "",
                id="target",
                style="display: flex; flex-direction: column;"
            )

serve()