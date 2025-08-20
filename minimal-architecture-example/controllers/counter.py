# controllers/counter.py

from fletx.core import FletXController, RxInt

class CounterController(FletXController):
    def __init__(self):
        self.count = RxInt(0)
        super().__init__()