class Trouble:
    def __init__(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def __str__(self):
        return '[Trouble {0}]'.format(self.__number)
