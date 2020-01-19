from decorator.display import StringDisplay, className
from decorator.border import FullBorder, SideBorder


def startMain():
    @FullBorder
    @SideBorder
    @StringDisplay
    def dummy1():
        className[2].show()
        className[1].show()
        className[0].show()
    dummy1()
    print("")
    className.clear()

    @SideBorder
    @FullBorder
    @FullBorder
    @SideBorder
    @FullBorder
    @StringDisplay
    def dummy2():
        className[0].show()
    dummy2()


if __name__ == '__main__':
    startMain()
