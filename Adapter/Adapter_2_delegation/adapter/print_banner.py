from adapter.banner import Banner
from adapter.print import Print


class PrintBanner(Print):
    def __init__(self, string):
        self.__banner = Banner(string)

    def printWeak(self):
        self.__banner.showWithParen()

    def printStrng(self):
        self.__banner.showWithAster()
