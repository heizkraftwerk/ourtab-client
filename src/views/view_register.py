import flet as ft
import requests

from .base import View


BACKEND_URL = "http://localhost:5150"


class ViewRegister(View):

    def compose(self) -> ft.View:
        input_username = ft.TextField(label="Username")
        input_email = ft.TextField(label="E-Mail")
        input_password = ft.TextField(
            label="Password", password=True, can_reveal_password=True
        )
        button_register = ft.ElevatedButton(
            "Register",
            on_click=lambda e: self.register(
                input_username.value, input_email.value, input_password.value
            ),
        )

        return ft.View(self.route, [input_username, input_email, input_password, button_register])

    @staticmethod
    def register(name: str, email: str, password: str) -> None:
        register_url = f"{BACKEND_URL}/api/auth/register"
        headers = {"Content-Type": "application/json"}
        request_data = {
            "name": name,
            "email": email,
            "password": password,
        }
        requests.post(register_url, headers=headers, json=request_data)
