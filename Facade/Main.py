from pagemaker.page_maker import PageMaker


def startMain():
    PageMaker.makeWelcomePage("hyuki@hyuki.com", "welcome1.html")
    PageMaker.makeWelcomePage("mamoru@hyuki.com", "welcome2.html")


if __name__ == '__main__':
    startMain()