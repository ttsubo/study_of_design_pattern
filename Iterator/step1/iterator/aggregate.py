from abc import ABCMeta, abstractmethod


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass
