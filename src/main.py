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

def route_change(page: ft.Page, route: str) -> None:
    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            [
                ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
            ],
        )
    )
    if page.route == "/store":
        page.views.append(
            ft.View(
                "/store",
                [
                    ft.AppBar(title=ft.Text("Store"), bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                    ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                ],
            )
        )
    page.update()

def view_pop(page: ft.Page, view) -> None:
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)

def register_view(page: ft.Page) -> None:
    input_username = ft.TextField(label="Username")
    input_email = ft.TextField(label="E-Mail")
    input_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
    button_register = ft.ElevatedButton("Register",
                                        on_click=lambda e: register(e, input_username.value, input_email.value,
                                                                    input_password.value))

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


def main(page: ft.Page):
    page.title = "Routes Example"

    page.on_route_change = lambda e: route_change(page, e)
    page.on_view_pop = lambda e: view_pop(page, e)
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)
