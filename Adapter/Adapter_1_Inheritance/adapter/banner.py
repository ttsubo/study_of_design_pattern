class Banner(object):
    def __init__(self, string):
        self.__string = string

    def showWithParen(self):
        print("({0})".format(self.__string))

    def showWithAster(self):
        print("*{0}*".format(self.__string))
