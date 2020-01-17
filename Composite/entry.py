from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    def add(self, entry):
        raise FileTreatmentException

    def printList(self):
        self._printList()

    @abstractmethod
    def _printList(self, prefix=''):
        pass

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def _printList(self, prefix=''):
        print("{0}/{1}".format(prefix, self))


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for d in self.directory:
            size += d.getSize()
        return size

    def add(self, entry):
        entry.path = self.name
        self.directory.append(entry)

    def _printList(self, prefix=''):
        print(prefix + "/" + str(self))
        for e in self.directory:
            e._printList(prefix + '/' + self.name)


class FileTreatmentException(Exception):
    def __init__(self,*args,**kwargs):
        self.message = "FileTreatmentException"
