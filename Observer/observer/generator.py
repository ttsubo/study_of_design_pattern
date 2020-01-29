import random
from abc import ABCMeta, abstractmethod


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def deleteObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObserver(self):
        for o in self.__observers:
            o.update(self)

    @abstractmethod
    def getNumber(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        self.__number = 0
        super(RandomNumberGenerator, self).__init__()

    def getNumber(self):
        return self.__number

    def execute(self):
        for _ in range(20):
            self.__number = random.randint(0, 49)
            self.notifyObserver()
