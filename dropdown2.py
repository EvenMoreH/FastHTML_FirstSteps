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
            Title("Dropdown testing"),
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
                    id="dropdown-button",
                    hx_get="/show",
                    hx_target="#dropdown-menu",
                    style="width: max(200px, 20%)",
                ),
            ),
            Div(
                id="dropdown-menu",
                style="display: flex; flex-direction: column;"
            ),
            Div(style="padding: 1rem"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div("TEXT TO SEE IF CONTENT WILL MOVE"),
            Div(style="padding: 1rem"),
            Button(
                "Next",
                hx_get="/output/{option}",
                hx_target="body",
                type="submit",
            style="width: max(200px, 20%)",
            )
        )
    )

@rt("/show")
def show():
    return Div(
                Button("A", hx_target="#dropdown-button", hx_get="/selected/A", hx_trigger="click", hx_swap="outerHTML"),
                Button("B", hx_target="#dropdown-button", hx_get="/selected/B", hx_trigger="click", hx_swap="outerHTML"),
                Button("C", hx_target="#dropdown-button", hx_get="/selected/C", hx_trigger="click", hx_swap="outerHTML"),
                id="dropdown-menu",
                style="display: flex; flex-direction: column; text-align: center; background: grey; width: max(200px, 20%); position: absolute;",
                # mouseleave trigger to hide content when mouse moves out of list of dropdown items
                hx_trigger="mouseleave delay:200ms",
                hx_get="/hide",
            )

@rt("/hide")
def hide():
    return Div(
                "",
                id="dropdown-menu",
                style="display: flex; flex-direction: column;"
            )

@rt("/selected/{option}")
def selected(session, option: str):
    session["chosen_type"] = option

    return Button(
        f"Option {option}",
        id="dropdown-button",
        hx_get="/show",
        hx_target="#dropdown-menu",
        hx_trigger="click",
        style="width: max(200px, 20%)",
        )

@rt("/output/{option}")
async def output(session, option:str):
    chosen_type = session.get("chosen_type", "No value set")
    if chosen_type == "A":
        item_type = "Armor"
    elif chosen_type == "B":
        item_type = "Weapon"
    else:
        item_type = "Misc"

    return Html(
        Head(
            Title("Dropdown testing"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org"),
            Link(rel="stylesheet", href="styles.css"),
            Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Button(
                f"Item type selected: {item_type} (Click to return)",
                hx_get="/",
                hx_target="body",
                style="width: max(200px, 20%)",
            )
        )
    )

serve()