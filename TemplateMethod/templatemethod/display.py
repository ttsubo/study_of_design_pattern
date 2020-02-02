from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.__ch = ch

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.__ch, end='')

    def close(self):
        print('>>')


class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.__string = string
        self.__width = len(string)

    def open(self):
        self.__printLine()

    def print(self):
        print("|{0}|".format(self.__string))

    def close(self):
        self.__printLine()

    def __printLine(self):
        print('+', end='')
        for _ in range(self.__width):
            print('-', end='')
        print('+')
