import sys
from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def createLink(self, caption, url):
        pass

    @abstractmethod
    def createTray(self, caption):
        pass

    @abstractmethod
    def createPage(self, title, author):
        pass


class Item(metaclass=ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def makeHtml(self):
        pass


class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption):
        super().__init__(caption)
        self.tray = []

    def add(self, item):
        self.tray.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def output(self):
        try:
            filename = self.title + '.html'
            writer = open(filename, 'w')
            writer.write(self.makeHtml())
            writer.close()
            print("[" + filename + "]" + " was created.")
        except Exception as e:
            print(e)
            sys.exit(1)

    @abstractmethod
    def makeHtml(self):
        pass
