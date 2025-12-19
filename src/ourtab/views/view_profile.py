import flet as ft
from flet.core.types import ImageFit

from .base import View


class ViewProfile(View):

    def compose(self) -> ft.View:

        grid = ft.GridView(
            controls=[
                ft.Image(src="https://picsum.photos/200", width=200, height=200, fit=ImageFit.COVER, border_radius=200),
            ],
            expand = True,
            max_extent = 350,
            spacing = 20,
            run_spacing = 20,
        )

        return ft.View(self.route, [grid])
