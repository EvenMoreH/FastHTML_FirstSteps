from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Titled, Link, Meta, Script, Redirect
)

# for Docker
# app, rt = fast_app(static_path="static") # type: ignore

# for local
app, rt = fast_app(static_path="app/static") # type: ignore


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
                    "Select Option",
                    id="dropdown-button",
                    hx_get="/show_dropdown",
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
                hx_get="/output/{button_option}",
                hx_target="body",
                type="submit",
            style="width: max(200px, 20%)",
            )
        )
    )

# handles selecting option from dropdown and fetches /hide options if cursor leaves menu
@rt("/show_dropdown")
def show():
    return Div(
                Button("A", hx_target="#dropdown-button", hx_get="/selected/A", hx_trigger="click", hx_swap="outerHTML"),
                Button("B", hx_target="#dropdown-button", hx_get="/selected/B", hx_trigger="click", hx_swap="outerHTML"),
                Button("C", hx_target="#dropdown-button", hx_get="/selected/C", hx_trigger="click", hx_swap="outerHTML"),
                id="dropdown-menu",
                style="display: flex; flex-direction: column; text-align: center; background: grey; width: max(200px, 20%); position: absolute;",
                # mouseleave trigger to hide content when mouse moves out of list of dropdown items
                hx_trigger="mouseleave delay:200ms",
                hx_get="/hide_dropdown",
            )

# handles hiding dropdown by setting it to empty string when mouseleave triggers on the list (login in /show_dropdown)
@rt("/hide_dropdown")
def hide():
    return Div(
                "",
                id="dropdown-menu",
                style="display: flex; flex-direction: column;"
            )

# handles displaying what option was selected from dropdown and casting it instead of dropdown button name
@rt("/selected/{button_option}")
def selected(session, button_option:str):
    session["button_option_selected"] = button_option

    return Button(
        f"Option {button_option}",
        id="dropdown-button",
        hx_get="/show_dropdown",
        hx_target="#dropdown-menu",
        hx_trigger="click",
        style="width: max(200px, 20%)",
        )

# example 'Next Page' that handles taking selected option and displaying it on 'new page' using session token
#   done to test carrying variables between endpoints
@rt("/output/{button_option}")
async def output(session, button_option:str):
    chosen_type = session.get("button_option_selected", "No value set")
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