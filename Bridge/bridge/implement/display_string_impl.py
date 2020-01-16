from bridge.implement.display_impl import DisplayImpl


class DisplayStringImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def rawOpen(self):
        self.printLine()

    def rawPrint(self):
        print("|{0}|".format(self.string))

    def rawClose(self):
        self.printLine()
        print("")

    def printLine(self):
        line = '-' * self.width
        print("+{0}+".format(line))
