from fasthtml.common import * # type: ignore

app, rt = fast_app() # type: ignore

@rt("/")
def redirect_to_login():
    return RedirectResponse("/example_page")

@rt("/example_page")
def example_page():
    page = Html(
        Head(
            Title('Example Page'),
            Link(rel="stylesheet", href="/examples/static/styles.css")
        ),
        Body(
            Div(
                'Some text on grey',
                cls='classA'
            ),
            Div(
                A('Clickable Link', href='https://example.com'),
                cls='classB'
            ),
            Div(
                Img(src="https://placehold.co/200"),
                cls='classA'
            ),
            Div(
                Button(
                    A("Go Green!", href="/green"),
                    cls='green_button',
                ),
                cls='classA'
            )
        )
    )
    return page

@rt("/green")
def green():
    page = Html(
        Head(
            Title('Example Page'),
            Link(rel="stylesheet", href="/examples/static/styles.css")
        ),
        Body(
            Div(
                'Some text on green',
                cls='classC'
            ),
            Div(
                A('Clickable Link', href='https://example.com'),
                cls='classC'
            ),
            Div(
                Img(src="https://placehold.co/200"),
                cls='classC'
            ),
            Div(
                Button(
                    A("Return", href="/example_page"),
                    cls='boring_button',
                ),
                cls='classC'
            )
        )
    )
    return page

serve() # type: ignore