import random
from bridge.function.display_func import DisplayFunc


class DisplayRandomFunc(DisplayFunc):
    def __init__(self, impl):
        super(DisplayRandomFunc, self).__init__(impl)

    def randomDisplay(self, times):
        self.open()
        t = random.randint(0, times)
        for _ in range(t):
            self.print_body()
        self.close()
