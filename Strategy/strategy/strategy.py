import random
from abc import ABCMeta, abstractmethod
from strategy.hand import Hand


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def nextHand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass


class WinningStrategy(Strategy):
    def __init__(self):
        self.__won = False
        self.__prevHand = None

    def nextHand(self):
        if not self.__won:
            self.__prevHand = Hand.getHand(random.randint(0, 2))
        return self.__prevHand

    def study(self, win):
        self.__won = win


class CircularStrategy(Strategy):
    def __init__(self):
        self.__Hand = 0

    def nextHand(self):
        return Hand.getHand(self.__Hand)

    def study(self, win):
        self.__Hand = (self.__Hand + 1) % 3
