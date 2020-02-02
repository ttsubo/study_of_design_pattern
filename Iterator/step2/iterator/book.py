class Book(object):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class BookShelf(object):
    def __init__(self):
        self.__books = []

    def append(self, book):
        self.__books.append(book)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__books):
            raise StopIteration()
        book = self.__books[self.__index]
        self.__index += 1
        return book
