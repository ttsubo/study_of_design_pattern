from templatemethod.display import CharDisplay, StringDisplay


def startMain():
    d1 = CharDisplay('H')
    d2 = StringDisplay("Hello, World!")
    d1.display()
    print("")
    d2.display()


if __name__ == '__main__':
    startMain()