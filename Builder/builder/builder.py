from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def makeTitle(self, title):
        pass

    @abstractmethod
    def makeString(self, str):
        pass

    @abstractmethod
    def makeItems(self, items):
        pass

    @abstractmethod
    def close(self):
        pass
