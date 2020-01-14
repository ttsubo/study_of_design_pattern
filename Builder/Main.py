import sys

from builder.director import Director
from builder.textbuilder.text_builder import TextBuilder
from builder.htmlbuilder.html_builder import HTMLBuilder


def startMain(opt):
    if opt == "plain":
        builder = TextBuilder()
        director = Director(builder)
        director.construct()
        result = builder.getResult()
        print(result)
    elif opt == "html":
        builder = HTMLBuilder()
        director = Director(builder)
        director.construct()
        result = builder.getResult()
        print("[" + result + "]" + " was created.")


if __name__ == "__main__":
    startMain(sys.argv[1])
