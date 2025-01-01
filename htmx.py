from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def homepage():
    return Html(
        Head(
            Title("TEST"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org"),
            Style(
                """
                * {
                    font-family: Georgia, 'Times New Roman', Times, serif;
                    font-size: clamp(1rem, 2vw, 3rem);
                    background-color: #1C1E1F;
                    color: rgb(225, 225, 225);
                }

                body {
                    min-height: 90vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    margin: auto;
                    padding: 0;
                    gap: 1vw;
                }
                """
            ),
            # Link(rel="stylesheet", href="styles.css"),
            # Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            # Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Titled("Click to reveal "),
            Button(
                "Click",
                hx_get="/reveal",
                hx_target="body"
            ),
            Button(
                "External",
                hx_get="/external",
            ),
        )
    )


@rt("/reveal")
def reveal():
    return Html(
            Head(
                Title("TEST"),
                Meta(name="viewport", content="width=device-width, initial-scale=1"),
                Script(src="https://unpkg.com/htmx.org"),
                # Link(rel="stylesheet", href="styles.css"),
                # Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
                # Link(rel="icon", href="images/favicon.png", type="image/png"),
            ),
            Body(
                Titled("Button was clicked"),
                P("This is my paragraph hidden behind a button click."),
                Button(
                    "Click",
                    hx_get="/",
                    hx_target="body"
                ),
                Button(
                    "External",
                    hx_get="/external",
                ),
            )
        )

@rt("/external")
def external():
    return Redirect("https://example.com")

serve()