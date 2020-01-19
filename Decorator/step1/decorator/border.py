from decorator.display import Display


class Border(Display):
    def __init__(self, display):
        self.display = display


class SideBorder(Border):
    def __init__(self, display, ch):
        super(SideBorder, self).__init__(display)
        self.__borderChar = ch

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return self.__borderChar + self.display.getRowText(row) + self.__borderChar


class FullBorder(Border):
    def __init__(self, display):
        super(FullBorder, self).__init__(display)

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
