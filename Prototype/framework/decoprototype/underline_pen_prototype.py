import copy
from framework.prototype import Prototype


class UnderlinePen(Prototype):
    def __init__(self, ulchar):
        self.__ulchar = ulchar

    def use(self, s):
        length = len(s)
        line = self.__ulchar * (length + 2)

        print("\"{0}\"".format(s))
        print("{0}\n".format(line))

    def createClone(self):
        clone = copy.deepcopy(self)
        return clone
