from adapter.banner import Banner
from adapter.print import Print


class PrintBanner(Banner, Print):
    def __init__(self, string):
        super(PrintBanner, self).__init__(string)

    def printWeak(self):
        self.showWithParen()

    def printStrng(self):
        self.showWithAster()
