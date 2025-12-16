import flet as ft
import requests

from .base import View


BACKEND_URL = "http://localhost:5150"


class ViewLogin(View):

    def compose(self) -> ft.View:
        input_email = ft.TextField(label="E-Mail")
        input_password = ft.TextField(
            label="Password", password=True, can_reveal_password=True
        )
        button_login = ft.ElevatedButton(
            "Login",
            on_click=lambda e: self.login(
                input_email.value, input_password.value
            ),
        )

        return ft.View(self.route, [input_email, input_password, button_login])

    @staticmethod
    def login(email: str, password: str) -> None:
        login_url = f"{BACKEND_URL}/api/auth/login"
        headers = {"Content-Type": "application/json"}
        request_data = {
            "email": email,
            "password": password,
        }
        requests.post(login_url, headers=headers, json=request_data)
