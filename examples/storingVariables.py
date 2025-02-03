from fasthtml.common import *

app, rt = fast_app(secret_key="your_secret_key")

# Route for the initial form
@rt("/")
def homepage(session):
    # Default type value from session if exists
    current_type = session.get('type', 'Not selected')
    return Titled("Select Type",
        Form(
            Fieldset(
                Label("Type A", Input(type="radio", name="type", value="A")),
                Label("Type B", Input(type="radio", name="type", value="B")),
                Label("Type C", Input(type="radio", name="type", value="C")),
            ),
            Button("Submit", type="submit"),
            method="post", action="/submit"
        ),
        P(f"Current selection: {current_type}"),
        Form(Button("Next", type="submit"),
            method="get", action="/next")
    )

# Route to handle form submission
@rt("/submit")
async def post(req, session):
    form = await req.form()  # Get form data
    selected_type = form.get("type")
    if selected_type:
        session['type'] = selected_type  # Store in session
        return RedirectResponse("/", status_code=303)  # Redirect back to form
    return Titled("Error", P("Please select a type."))

# Route for subsequent actions
@rt("/next")
def next(session):
    selected_type = session.get('type', 'Not selected')
    return Titled("Next Page", P(f"Type selected in previous step: {selected_type}"))

serve()