from abc import ABCMeta, abstractmethod


class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def rawOpen(self):
        pass

    @abstractmethod
    def rawPrint(self):
        pass

    @abstractmethod
    def rawClose(self):
        pass