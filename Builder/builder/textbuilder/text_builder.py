from builder.builder import Builder


class TextBuilder(Builder):
    def __init__(self):
        self.buffer = []

    def makeTitle(self, title):
        self.buffer.append("======================\n")
        self.buffer.append(title + "\n")
        self.buffer.append("\n")

    def makeString(self, str):
        self.buffer.append("*** " + str + " ***" + "\n")

    def makeItems(self, items):
        for i in items:
            self.buffer.append("- " + i + "\n")

    def close(self):
        self.buffer.append("======================\n")

    def getResult(self):
        return ''.join(self.buffer)