from decorator.display import StringDisplay_filter, className
from decorator.border import SideBorder_filter, FullBorder


def startMain():
    @FullBorder
    @SideBorder_filter('#')
    @StringDisplay_filter("Hello, world.")
    def dummy1():
        className[2].show()
        className[1].show()
        className[0].show()
    dummy1()
    print("")
    className.clear()

    @SideBorder_filter('/')
    @FullBorder
    @FullBorder
    @SideBorder_filter('*')
    @FullBorder
    @StringDisplay_filter("HELLO")
    def dummy2():
        className[0].show()
    dummy2()


if __name__ == '__main__':
    startMain()
