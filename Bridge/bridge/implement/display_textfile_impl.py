from bridge.implement.display_impl import DisplayImpl


class DisplayTextfileImpl(DisplayImpl):
    def __init__(self, filename):
        self.filename = filename

    def rawOpen(self):
        filename = self.filename
        self.f = open(filename, "r")

    def rawPrint(self):
        data = self.f.read()
        data = data.split('\n')
        for l in data:
            print(l)

    def rawClose(self):
        self.f.close()
