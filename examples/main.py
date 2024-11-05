from fasthtml.common import *

app,rt = fast_app()

# Displays Hello World! when localhost is visited
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

# Displays Nice to be here! when Hello World! is clicked
@rt('/change')
def get(): return P('Nice to be here!')

serve()