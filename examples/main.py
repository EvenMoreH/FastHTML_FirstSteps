from fasthtml.common import * # type: ignore

app,rt = fast_app() # type: ignore

# Displays Hello World! when localhost is visited
@rt('/')
def get1(): return Div(P('Hello World!'), hx_get="/change")

# Displays Nice to be here! when Hello World! is clicked
@rt('/change')
def get2(): return P('Nice to be here!')

serve() # type: ignore