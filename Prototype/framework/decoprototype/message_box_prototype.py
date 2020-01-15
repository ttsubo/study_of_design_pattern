import copy
from framework.prototype import Prototype


class MessageBox(Prototype):
    def __init__(self, decochar):
        self.__decochar = decochar

    def use(self, s):
        length = len(s)
        line = self.__decochar * (length + 4)

        print("{0}".format(line))
        print("{0} {1} {2}".format(self.__decochar, s, self.__decochar))
        print("{0}\n".format(line))

    def createClone(self):
        clone = copy.deepcopy(self)
        return clone
