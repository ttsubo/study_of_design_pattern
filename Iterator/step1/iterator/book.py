from iterator.iterator import Iterator
from iterator.aggregate import Aggregate


class Book(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class BookShelfIterator(Iterator):
    def __init__(self, bookShelf):
        self.__bookShelf = bookShelf
        self.__index = 0

    def hasNext(self):
        return True if self.__index < self.__bookShelf.getLength() else False

    def next(self):
        book = self.__bookShelf.getBookAt(self.__index)
        self.__index += 1
        return book


class BookShelf(Aggregate):
    def __init__(self, maxSize):
        self.__last = 0
        self.__books = [None] * maxSize

    def getBookAt(self, index):
        return self.__books[index]

    def append(self, book):
        self.__books[self.__last] = book
        self.__last += 1

    def getLength(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
