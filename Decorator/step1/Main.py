from decorator.display import StringDisplay
from decorator.border import SideBorder, FullBorder


def startMain():
    b1 = StringDisplay('Hello, world.')
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()
    print("")
    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay('HELLO')
                    ),
                    '*'
                )
            )
        ),
        '/'
    )
    b4.show()


if __name__ == '__main__':
    startMain()
