# Example of flet counter app
import flet as ft

def main(page: ft.Page):
    counter = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT)
    
    def increment(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    page.add(
        ft.Column([
            counter,
            ft.ElevatedButton("Increment", on_click=increment)
        ])
    )

ft.app(target=main)