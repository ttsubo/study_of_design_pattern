from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v):
        pass


class Entry(Element):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    def add(self, entry):
        raise FileTreatmentException

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())


class File(Entry):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def accept(self, v):
        v.visit(self)


class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.__dir = []

    def getName(self):
        return self.__name

    def getSize(self):
        size = 0
        for f in self.__dir:
            size += f.getSize()
        return size

    def add(self, entry):
        self.__dir.append(entry)
        return self
    
    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__dir):
            raise StopIteration()
        dir = self.__dir[self.__index]
        self.__index += 1
        return dir

    def accept(self, v):
        v.visit(self)


class FileTreatmentException(Exception):
    def __init__(self,*args,**kwargs):
        self.message = "FileTreatmentException"
