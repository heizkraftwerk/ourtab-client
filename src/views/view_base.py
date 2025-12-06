import flet as ft

from .base import View


class ViewBase(View):

    def __init__(self):
        super().__init__("/")

    def compose(self) -> ft.View:
        return ft.View(
            self.route,
            [
                ft.ElevatedButton("Visit Store"),
            ],
        )
