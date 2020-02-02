from iterator.book import Book, BookShelf


def startMain():
    bookShelf = BookShelf()
    bookShelf.append(Book(name="Aroun d the World in 80 days"))
    bookShelf.append(Book(name="Bible"))
    bookShelf.append(Book(name="Cinderella"))
    bookShelf.append(Book(name="Daddy-Long-Legs"))
    for book in bookShelf:
        print(book.getName())


if __name__ == '__main__':
    startMain()
