import random
from flet import *
from fletx.app import FletXApp
from fletx.core import RxList, FletXPage
from fletx.decorators import reactive_list
from fletx.navigation import router_config

@reactive_list(
    items_attr='rx_items',
    item_builder=lambda item, index: ListTile(
        title=Text(f'Title Item {item}'),
        subtitle=Text(f'Subtitle of Item {item}')
    ),
    empty_builder=lambda: Container(
        expand=True,
        content=Column(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Image(src='empty.png'),
                Text('The list is empty')
            ]
        )
    ),
    animate_changes=True
)
class ListComponent(ListView):
    def __init__(self, rx_items: RxList = RxList([]), **kwargs):
        self.rx_items = rx_items
        super().__init__(expand=True, spacing=20, **kwargs)

class MyPage(FletXPage):
    def __init__(self):
        super().__init__()
        self.items = RxList([1, 2, 3])

    def build(self):
        return SafeArea(
            content=Column(
                controls=[
                    Text("Reactive List Demo", size=18, weight=FontWeight.BOLD),
                    Container(
                        height=400,
                        content=ListComponent(rx_items=self.items)
                    ),
                    Row(
                        spacing=20,
                        controls=[
                            TextButton("Clear", on_click=lambda _: self.items.clear()),
                            TextButton("Remove Last", on_click=lambda _: self.items.pop()),
                            TextButton("Add Random", on_click=lambda _: self.items.append(random.randint(0,100)))
                        ]
                    )
                ]
            )
        )
  
def main():
      router_config.add_route(path="/", component=MyPage)
    
      app = FletXApp(
          initial_route="/",
          theme_mode=ThemeMode.DARK,
          theme=Theme(color_scheme_seed=Colors.GREEN),
      ).with_window_size(400, 810)
    
      app.run_async()

if __name__ == "__main__":
    main()