from iterator.book import Book, BookShelf


def startMain():
    bookShelf = BookShelf(4)
    bookShelf.append(Book(name="Aroun d the World in 80 days"))
    bookShelf.append(Book(name="Bible"))
    bookShelf.append(Book(name="Cinderella"))
    bookShelf.append(Book(name="Daddy-Long-Legs"))
    it = bookShelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.getName())


if __name__ == '__main__':
    startMain()
