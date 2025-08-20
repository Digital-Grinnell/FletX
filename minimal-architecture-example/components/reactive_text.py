# components/reactive_text.py

import flet as ft
from fletx.decorators import simple_reactive
from fletx.core import RxStr


@simple_reactive(bindings={'value': 'text'})
class MyReactiveText(ft.Text):

    def __init__(self, rx_text: RxStr, **kwargs):
        self.text: RxStr = rx_text
        super().__init__(**kwargs)