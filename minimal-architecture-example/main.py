# main.py

from fletx.app import FletXApp
from fletx.navigation import router_config
from pages.counter import CounterPage

router_config.add_route("/", CounterPage)

app = FletXApp(title="Demo App")
app.run()

