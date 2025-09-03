import requests

import flet as ft
from flet.core.control_event import ControlEvent

BACKEND_URL = "http://localhost:5150"


def register(event: ControlEvent, name: str, email: str, password: str) -> None:
    register_url = f"{BACKEND_URL}/api/auth/register"
    headers = {"Content-Type": "application/json"}
    request_data = {
        "name": name,
        "email": email,
        "password": password,
    }
    requests.post(register_url, headers=headers, json=request_data)


def main(page: ft.Page):
    input_username = ft.TextField(label="Username")
    input_email = ft.TextField(label="E-Mail")
    input_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    button_register = ft.ElevatedButton("Register", on_click=lambda e: register(e, input_username.value, input_email.value, input_password.value))


    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    input_username,
                    input_email,
                    input_password,
                    button_register
                ]
            )
        )
    )


ft.app(main)
