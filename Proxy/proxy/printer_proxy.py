import sys
import time
from abc import ABCMeta, abstractmethod


class Printable(metaclass=ABCMeta):
    @abstractmethod
    def setPrinterName(self, name):
        pass

    @abstractmethod
    def getPrinterName(self):
        pass

    @abstractmethod
    def myPrint(self, string):
        pass


class Printer(Printable):
    @classmethod
    def getPrinter(cls, name):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(name)
        else:
            cls._instance.__name = name
        return cls._instance

    def __init__(self, name):
        self.__name = name
        self.__heavyJob('Printerのインスタンス({})を作成中'.format(self.__name))

    def setPrinterName(self, name):
        self.__name = name

    def getPrinterName(self):
        return self.__name

    def myPrint(self, string):
        print('=== Printer使用者({}) ==='.format(self.__name))
        print(string)
        print("")

    def __heavyJob(self, msg):
        print(msg, end='')
        for _ in range(10):
            time.sleep(1)
            print('.', end='')
        print('完了')


class PrinterProxy(Printable):
    def __init__(self, name):
        self.__name = name
        self.__real = None

    def setPrinterName(self, name):
        self.__name = name

    def getPrinterName(self):
        return self.__name

    def myPrint(self, string):
        self.__real = Printer.getPrinter(self.__name)
        self.__real.myPrint(string)
