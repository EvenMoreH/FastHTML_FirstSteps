from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    dropdown_script = Script("""
        document.addEventListener('click', function(event) {
            let dropdown = document.querySelector('.dropdown-menu');
            let button = document.querySelector('.dropdown-button');

            if (button.contains(event.target)) {
                dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
            } else if (!dropdown.contains(event.target)) {
                dropdown.style.display = 'none';
            }
        });

        document.querySelectorAll('.dropdown-item').forEach(item => {
            item.addEventListener('click', function() {
                let selectedDiv = document.getElementById('selected');
                selectedDiv.textContent = 'Selected: ' + this.textContent;
                document.querySelector('.dropdown-menu').style.display = 'none';
            });
        });
    """)

    dropdown = Div(
        Div(
            Button("Dropdown Menu", cls="dropdown-button"),
            Div(
                Div("Option 1", cls="dropdown-item"),
                Div("Option 2", cls="dropdown-item"),
                Div("Option 3", cls="dropdown-item"),
                cls="dropdown-menu",
                style="display: none; position: absolute; background: #fff; border: 1px solid #ccc; padding: 10px; cursor: pointer;"
            ),
            style="position: relative;"
        ),
        Div(id="selected", style="margin-top: 20px;"),
        dropdown_script,
        cls="dropdown-container"
    )

    return Titled("Dropdown Example", dropdown)

serve()