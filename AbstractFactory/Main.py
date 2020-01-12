import sys
import inspect
import factory


def startMain(factoryObject):
    asahi = factoryObject.createLink("Asahi", "http://www.asahi.com")
    yomiuri = factoryObject.createLink("Yomiuri", "http://www.yomiuri.co.jp")
    us_yahoo = factoryObject.createLink("Yahoo", "http://www.yahoo.com")
    jp_yahoo = factoryObject.createLink("Yahoo!Japan", "http://www.yahoo.co.jp")
    google = factoryObject.createLink("Google", "http://www.google.com")
    excite = factoryObject.createLink("Excite", "http://www.excite.co.jp")

    traynews = factoryObject.createTray("Newspaper")
    traynews.add(asahi)
    traynews.add(yomiuri)

    trayyahoo = factoryObject.createTray("Yahoo!")
    trayyahoo.add(us_yahoo)
    trayyahoo.add(jp_yahoo)

    traysearch = factoryObject.createTray("Search Engine")
    traysearch.add(trayyahoo)
    traysearch.add(excite)
    traysearch.add(google)

    page = factoryObject.createPage("LinkPage", "Hiroshi Yuki")
    page.add(traynews)
    page.add(traysearch)
    page.output()


if __name__ == '__main__':
    for _, plugin in inspect.getmembers(factory, inspect.isclass):
        if plugin.__name__ == sys.argv[1]:
            startMain(plugin())
