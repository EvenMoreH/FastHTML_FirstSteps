from fasthtml.common import *
from dataclasses import dataclass
from typing import Optional

# # #
# Learning forms and databases
# # #

app, rt = fast_app(debug=True)

# we built dataclass for user_profile
@dataclass
class Car:
    make: str
    model: str
    fuel: str
    id: Optional[int] = None

# we build user profile form that handles data specified in dataclass as well as handles submit
new_car_form = Form(
    method="post",
    action="/car"
    )(
        Fieldset(
            Label("Make", Input(name="make")),
            Label("Model", Input(name="model")),
            Label("Fuel Type", Input(name="fuel")),
        ),
        Button("Save", type="submit"),
    )

# creating simple database
db = database("db_1/cars.db")
cars_db = db.create(Car, pk="id")

# insert sample car only if database is empty
if not list(cars_db()):
    new_car = Car(make="BMW", model="M3", fuel="gas")
    cars_db.insert(new_car)


# endpoint to see what is going on
@rt("/car/{id}")
def car(id: int):
    Car = cars_db[id]
    # fill form is a method that: Fills named items in form using attributes in obj
    filled_new_car_form = fill_form(new_car_form, Car)

    return Titled(f"Profile of: [{Car.make} {Car.model}]", filled_new_car_form)


@rt("/new_car", methods=["POST", "UPDATE", "GET"])
def new_car(new_car: Car):
    # creating a car object to be added to database
    new_car = dict(make="BMW", model="Q12", fuel="electric")
    # creating a variable to store what was added to database exactly
    added_car = cars_db.insert(new_car)
    # extracting car_id from a variable that stores what was added to database
    car_id = added_car.id
    # redirecting to page of just added car
    return RedirectResponse(url=f"/car/{car_id}")


@rt("/all_cars", methods=["GET"])
def cars():
    all_cars = cars_db()
    all_cars_list = Ul(*[Li(f"{vehicle.make} {vehicle.model} {vehicle.fuel}") for vehicle in all_cars])

    return Titled("All cars:", Div(all_cars_list))


serve()