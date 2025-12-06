import flet as ft

from views import ViewBase, ViewManager, ViewRegister, ViewLogin


def main(page: ft.Page):
    page.title = "Routes Example"

    view_base = ViewBase(page=page)
    view_login = ViewLogin("/login", page=page)
    view_register = ViewRegister("/register", page=page)
    view_manager = ViewManager(page, view_base, [view_register, view_login])

    page.on_route_change = lambda e: view_manager.on_route_change(e)
    page.on_view_pop = lambda e: view_manager.on_view_pop(e)
    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)
