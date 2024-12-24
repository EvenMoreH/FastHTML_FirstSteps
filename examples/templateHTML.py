from fasthtml.common import * # type: ignore

app, rt = fast_app() # type: ignore

@rt("/")
def home():
    page = Html(
        Head(
            Title('Example Page'),
            Link(rel="stylesheet", href="/examples/static/styles.css")
        ),
        Body(
            Div(
                'Some text,',
                cls='classA'
            ),
            Div(
                A('Clickable Link', href='https://example.com'),
                cls='classB'
            ),
            Div(
                Img(src="https://placehold.co/200"),
                cls='classA'
            )
        )
    )
    return page

serve() # type: ignore