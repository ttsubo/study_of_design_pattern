from abc import ABCMeta, abstractmethod


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass
