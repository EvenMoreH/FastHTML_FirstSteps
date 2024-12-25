from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Form, Fieldset, Label, Input, Button, Html, Head, Body, P, Title, RedirectResponse
)
from dataclasses import dataclass
from typing import Optional
from fastlite import Database # type: ignore
from fastcore.utils import * # type: ignore
from fastcore.net import * # type: ignore

app, rt = fast_app() # type: ignore

# dataclass for User entry in database
#   id: Optional[int] = None at the end as it is autoincrement by the system
@dataclass
class User:
    email:str
    name:str
    age:int
    id: Optional[int] = None

# database creation
#   always create database before creating schema and primary_key (pk)
db = Database("examples/pos_get_db/users.db")
users_table = db.create(User, pk="id")

# user form variable holding fields and buttons
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

# main page with user form displayed
@rt("/")
def home():
    return Html(
        Head(
            Title("User Registration")
        ),
        Body(
            Titled("Register User", user_form)
        )
    )

# submitting user form
@rt("/submit")
def submit(email: str, name: str, age: int):
    try:
        user = User(email=email, name=name, age=int(age))
        users_table.insert(user)

        return RedirectResponse("/users")

    except Exception as e:
        return Html(
            Head(
                Title("Error")
            ),
            Body(
                P(f"Error saving user: {e}")
            )
        )

# endpoint to display all users in DB
@rt("/users")
def users():
    all_users = users_table()
    user_list = Ul(*[Li(f"{u.id}. {u.name} ({u.email}), Age: {u.age}") for u in all_users])

    return Html(
        Head(
            Title("Registered Users")
        ),
        Body(
            Titled("User List", user_list)
        )
    )

serve() # type: ignore