from abc import ABCMeta, abstractmethod

className = []


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
    def __init__(self, func):
        self.string = "Hello, world."
        self.func = func
        super(StringDisplay, self).__init__()

    def getColumns(self):
        return len(self.string)

    def getRows(self):
        return 1

    def getRowText(self, row):
        if row == 0:
            return self.string
        else:
            return None
    
    def __call__(self):
        global className
        className.append(self)
        return self.func()
