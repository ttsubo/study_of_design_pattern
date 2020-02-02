from abc import ABCMeta, abstractmethod
from visitor.element import Directory


class Vistor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, directory):
        pass


class ListVistor(Vistor):
    def __init__(self):
        self.__currentdir = ''

    def visit(self, directory):
        print("{0}/{1}".format(self.__currentdir, directory))
        if isinstance(directory, Directory):
            savedir = self.__currentdir
            self.__currentdir = self.__currentdir + '/' + directory.getName()
            for f in directory:
                f.accept(self)
            self.__currentdir = savedir
