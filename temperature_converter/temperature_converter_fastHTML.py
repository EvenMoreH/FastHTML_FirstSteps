from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Form, Fieldset, Label, Input, Button, Html, Head, Body, Div, P, Title, Titled, A, RedirectResponse
)
app, rt = fast_app() # type: ignore

temperature_form = Form(
    method = "post",
    action = "/convert"
    )(
    Fieldset(
        Label("Temperature", Input(name="temperature", type="number", required=True))
    ),
    Div(
        Button("Kelvin -> Celsius", name="conversion", value="kc", type="submit"),
        cls="button1"
    ),
    Div(
        Button("Kelvin -> Fahrenheit", name="conversion", value="kf", type="submit"),
        cls="button1"
    ),
    Div(
        Button("Fahrenheit -> Celsius", name="conversion", value="fc", type="submit"),
        cls="button1"
    ),
    Div(
        Button("Fahrenheit -> Kelvin", name="conversion", value="fk", type="submit"),
        cls="button1"
    ),
    Div(
        Button("Celsius -> Fahrenheit", name="conversion", value="cf", type="submit"),
        cls="button1"
    ),
    Div(
        Button("Celsius -> Kelvin", name="conversion", value="ck", type="submit"),
        cls="button1"
    ),
)

@rt("/")
def homepage():
    return Html(
        Head(
            Title("Temperature Converter"),
            Link(rel="stylesheet", href="temperature_converter/styles1.css")
        ),
        Body(
            Div(
                temperature_form
            )
        )
    )

@rt("/convert", methods=["POST"])
def convert_temperature(temperature:float, conversion:str):
    if conversion == "kc":
        kc = temperature + 273.15
        result = f"{temperature} in Kelvin equals to {kc:.2f}°C"
    elif conversion == "kf":
        kf = ((temperature - 273.15) * (9/5)) + 32
        result = f"{temperature} in Kelvin equals to {kf:.2f}°F"
    elif conversion == "fc":
        fc = (temperature - 32) * (5/9)
        result = f"{temperature} in Fahrenheit equals to {fc:.2f}°C"
    elif conversion == "fk":
        fk = ((temperature - 32) * (5/9)) + 273.15
        result = f"{temperature} in Fahrenheit equals to {fk:.2f}°K"
    elif conversion == "cf":
        cf = (temperature * (9/5)) + 32
        result = f"{temperature} in Celsius equals to {cf:.2f}°F"
    elif conversion == "ck":
        ck = temperature - 273.15
        result = f"{temperature} in Celsius equals to {ck:.2f}°K"


    return Html(
        Head(
            Title("Conversion Results")
        ),
        Body(
            Titled("Conversion Results"),
            P(result),
            Button(
                A("Return to Form", href="/"),
                cls="button1"
            )
        )
    )

serve() # type: ignore