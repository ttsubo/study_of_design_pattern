from decorator.display import Display, className


class Border(Display):
    def __init__(self, display):
        self.display = display
        super(Border, self).__init__()


class SideBorder(Border):
    def __init__(self, func):
        self.func = func
        self.__borderChar = '#'
        super(SideBorder, self).__init__(func)

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return self.__borderChar + self.display.getRowText(row) + self.__borderChar
    
    def __call__(self):
        global className
        className.append(self)
        return self.func()


class FullBorder(Border):
    def __init__(self, func):
        self.func = func
        super(FullBorder, self).__init__(func)

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return 1 + self.display.getRows() + 1

    def getRowText(self, row):
        if row == 0:
            return '+' + self.__make_line('-', self.display.getColumns()) + '+'
        elif row == self.display.getRows() + 1:
            return '+' + self.__make_line('-', self.display.getColumns()) + '+'
        else:
            return '|' + self.display.getRowText(row - 1) + '|'

    def __make_line(self, char, count):
        buf = ''
        for _ in range(count):
            buf += char
        return buf

    def __call__(self):
        global className
        className.append(self)
        return self.func()
