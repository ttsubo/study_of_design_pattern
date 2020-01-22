import sys
from flyweight.big_char_factory import BigCharFactory, BigString

def startMain(string):
    bs = BigString(string)
    bs.print()


if __name__ == '__main__':
    startMain(sys.argv[1])