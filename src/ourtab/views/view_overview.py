import flet as ft

from .base import View
from ..utils import Color

class ViewOverview(View):

    def compose(self) -> ft.View:

        # Saldo
        saldo_container = ft.Container(
            content=ft.Text(
                "Gesamt Saldo",
                size=24,
                weight=ft.FontWeight.BOLD,
                color=Color.PRIMARY_FOREGROUND.value),
            padding=20,
            alignment=ft.alignment.center,
            bgcolor=Color.PRIMARY.value,
            width=float("inf"),
            height=150,
            border_radius=12,
            ink=True,
            on_click=lambda e: print("Go to gesamt saldo")
        )

        # Group container
        def group_container(title: str) -> ft.Container:
            return ft.Container(
                content=ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.W_600,
                    color=Color.CARD_FOREGROUND.value),
                padding=20,
                alignment=ft.alignment.center,
                bgcolor=Color.CARD.value,
                width=300,
                height=150,
                border_radius=12
            )

        # Example groups
        groups_example = ["Gruppe A", "Gruppe B", "Gruppe C", "Gruppe D", "Gruppe E"]

        # Group grid layout
        grid = ft.GridView(
            expand=True,
            max_extent=350,
            child_aspect_ratio=2,
            spacing=20,
            run_spacing=20,
        )

        for g in groups_example:
            grid.controls.append(group_container(g))

        content = ft.Column(
            [
                saldo_container,
                grid
            ],
            expand=True,
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        )

        return ft.View(self.route, [content])

