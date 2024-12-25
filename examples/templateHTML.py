from fasthtml.common import * # type: ignore
from dataclasses import dataclass
from fastlite import Database # type: ignore
from fastcore.utils import *
from fastcore.net import *

app, rt = fast_app() # type: ignore

@dataclass
class User:
    id: int
    email:str
    name:str
    age:int

db = Database("users.db")
users_table = db.create(User, pk="email")


user_form = Form(
    method="post",
    action="/submit"
)(
    Fieldset(
        Label("Email", Input(name="email")),
        Label("Name", Input(name="name")),
        Label("Age", Input(name="age", type="number"))
    ),
    Button("Submit", type="submit")
)

# Route to display the form
@rt("/")
def home():
    return Html(
        Head(Title("User Registration")),
        Body(
            Titled("Register User", user_form)
        )
    )

# @rt("/")
# def redirect_to_login():
#     return RedirectResponse("/example_page")

# Route to handle form submission and save to the database
@rt("/submit")
def submit(email: str, name: str, age: int):
    try:
        user = User(email=email, name=name, age=int(age))  # Create a User instance
        users_table.insert(user)  # Insert into the database
        return RedirectResponse("/users")  # Redirect to user list
    except Exception as e:
        return Html(
            Head(Title("Error")),
            Body(P(f"Error saving user: {e}"))
        )

# Route to display all users from the database
@rt("/users")
def users():
    all_users = users_table()
    user_list = Ul(*[Li(f"{u.name} ({u.email}), Age: {u.age}") for u in all_users])
    return Html(
        Head(Title("Registered Users")),
        Body(
            Titled("User List", user_list),
        )
    )

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