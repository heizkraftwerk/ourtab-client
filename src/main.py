import flet as ft

from views import ViewBase, ViewManager, ViewRegister


def main(page: ft.Page):
    page.title = "Routes Example"

    view_base = ViewBase()
    view_register = ViewRegister("/register")
    view_manager = ViewManager(page, view_base, [view_register])

    page.on_route_change = lambda e: view_manager.on_route_change(e)
    page.on_view_pop = lambda e: view_manager.on_view_pop(e)
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)
