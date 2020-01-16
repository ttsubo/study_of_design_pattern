from bridge.function.display_func import DisplayFunc


class DisplayCountFunc(DisplayFunc):
    def __init__(self, impl):
        super(DisplayCountFunc, self).__init__(impl)

    def multiDisplay(self, times):
        self.open()
        for _ in range(times):
            self.print_body()
        self.close()
