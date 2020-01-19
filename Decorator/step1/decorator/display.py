from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):
    @abstractmethod
    def getColumns(self):
        pass

    @abstractmethod
    def getRows(self):
        pass

    @abstractmethod
    def getRowText(self, row):
        pass

    def show(self):
        for i in range(self.getRows()):
            print(self.getRowText(i))


class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def getColumns(self):
        return len(self.string)

    def getRows(self):
        return 1

    def getRowText(self, row):
        if row == 0:
            return self.string
        else:
            return None
