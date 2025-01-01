from fasthtml.common import *

app, rt = fast_app()

# Simulated database
db = {}


@rt("/")
def get():
    # Display all links with toggling functionality
    links = [
        Div(
            A(
                "example.com",
                hx_get=f"/toggle/{id}/obfuscate",
                hx_swap="outerHTML"
            ),
            id=f"link-{id}"
        )
        for id in db
    ]
    return Titled(
        "Toggle Links",
        *links,
        Form(
            Input(name="link", placeholder="Enter link"),
            Button("Submit", type="submit"),
            method="post",
            action="/store"
        )
    )


@rt("/store")
def post(link: str):
    # Store the actual link with an ID
    id = len(db)
    db[id] = link
    return RedirectResponse("/", status_code=303)


@rt("/toggle/{id:int}/{state:str}")
def get(id: int, state: str):
    # Toggle between obfuscated and real link
    if id not in db:
        return Div("Link not found", cls="error")

    if state == "obfuscate":
        return A(
            "example.com",
            hx_get=f"/toggle/{id}/reveal",
            hx_swap="outerHTML",
            id=f"link-{id}"
        )
    elif state == "reveal":
        return A(
            db[id],
            hx_get=f"/toggle/{id}/obfuscate",
            hx_swap="outerHTML",
            id=f"link-{id}"
        )


serve()
