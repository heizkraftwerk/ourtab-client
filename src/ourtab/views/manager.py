from dataclasses import dataclass
from typing import List, Optional

import flet as ft
from flet.core.control_event import ControlEvent
from flet.core.cupertino_icons import CupertinoIcons
from flet.core.icons import Icons

from .base import View
from .view_base import ViewBase


@dataclass
class NavigationItem:
    route: str
    label: str
    icon: Optional[str|Icons|CupertinoIcons]


class ViewManager:

    def __init__(self, page: ft.Page, base_view: ViewBase, views: List[View]):
        self._page = page
        self._views = views
        self._base_view = base_view
        self._navigation_items = [
            NavigationItem(route="/", label="Overview", icon=ft.Icons.DASHBOARD),
            NavigationItem(route="/login", label="Add", icon=ft.Icons.ADD),
            NavigationItem(route="/profile", label="Profile", icon=ft.Icons.ACCOUNT_CIRCLE),
        ]

        self._navigation_bar = self._get_navigation_bar()
        self._page.navigation_bar = self._navigation_bar
        self._page.update()

    def _get_navigation_destinations(self) -> List[ft.NavigationBarDestination]:
        return [ft.NavigationBarDestination(icon=dest.icon, label=dest.label) for dest in self._navigation_items]

    def _get_navigation_bar(self) -> ft.NavigationBar:
        return ft.NavigationBar(
            destinations=self._get_navigation_destinations(),
            on_change=lambda index: self._navigation_bar_change(index)
        )

    def _navigation_bar_change(self, event: ControlEvent) -> None:
        index = int(event.data)
        route = self._navigation_items[index].route
        self._page.go(route)
        self._navigation_bar.selected_index = index

    def _compose_view(self, view: View) -> ft.View:
        view = view.compose()
        view.navigation_bar = self._navigation_bar
        return view

    def on_route_change(self, event: ft.RouteChangeEvent):
        self._page.views.clear()

        self._page.views.append(self._compose_view(self._base_view))
        for view in self._views:
            if self._page.route == view.route:
                self._page.views.append(self._compose_view(view))

        self._page.update()

    def on_view_pop(self, view) -> None:
        self._page.views.pop()
        top_view = self._page.views[-1]
        self._page.go(top_view.route)
