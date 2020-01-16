from bridge.function.display_func import DisplayFunc
from bridge.function.display_count_func import DisplayCountFunc
from bridge.function.display_random_func import DisplayRandomFunc
from bridge.implement.display_string_impl import DisplayStringImpl
from bridge.implement.display_textfile_impl import DisplayTextfileImpl


def startMain():
    d1 = DisplayFunc(DisplayStringImpl("Hello Japan"))
    d2 = DisplayCountFunc(DisplayStringImpl("Hello Japan"))
    d3 = DisplayCountFunc(DisplayStringImpl("Hello Universe"))
    d4 = DisplayRandomFunc(DisplayStringImpl("Hello Universe"))
    d5 = DisplayFunc(DisplayTextfileImpl("test.txt"))
    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)
    d4.randomDisplay(5)
    d5.display()


if __name__ == '__main__':
    startMain()
