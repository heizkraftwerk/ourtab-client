import flet as ft

from .base import View


class ViewBase(View):

    def __init__(self, page: ft.Page):
        super().__init__("/", page=page)

    def compose(self) -> ft.View:
        return ft.View(
            self.route,
            [
                ft.ElevatedButton("Register", on_click=lambda e: self._page.go("/register")),
            ],
        )
