from abc import ABC, abstractmethod

import flet as ft


class View(ABC):

    def __init__(self, route: str):
        self._route = route

    @property
    def route(self) -> str:
        return self._route

    @abstractmethod
    def compose(self) -> ft.View:
        """Compose the controls that make up the view and return them as a list."""
