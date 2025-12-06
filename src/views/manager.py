from typing import List

import flet as ft

from .base import View
from .view_base import ViewBase


class ViewManager:

    def __init__(self, page: ft.Page, base_view: ViewBase, views: List[View]):
        self._page = page
        self._views = views
        self._base_view = base_view

    def on_route_change(self, event: ft.RouteChangeEvent):
        self._page.views.clear()

        self._page.views.append(self._base_view.compose())
        for view in self._views:
            if self._page.route == view.route:
                self._page.views.append(view.compose())

        self._page.update()

    def on_view_pop(self, view) -> None:
        self._page.views.pop()
        top_view = self._page.views[-1]
        self._page.go(top_view.route)
