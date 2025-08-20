# pages/counter.py

from fletx.core import FletXPage
from controllers.counter import CounterController
from components.reactive_text import MyReactiveText
import flet as ft

class CounterPage(FletXPage):
    ctrl = CounterController()

    def build(self):
        return ft.Column([
            MyReactiveText(rx_text=self.ctrl.count, size=40, weight="bold"),
            ft.ElevatedButton("Increment", on_click=lambda e: self.ctrl.count.increment())
        ])