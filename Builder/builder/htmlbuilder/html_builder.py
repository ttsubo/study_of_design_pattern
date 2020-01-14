from builder.builder import Builder


class HTMLBuilder(Builder):
    def __init__(self):
        self.buffer = []
        self.filename = ""
        self.f = None
        self.makeTitleCalled = False

    def makeTitle(self, title):
        self.filename = title+".html"
        self.f = open(self.filename, "w")
        self.f.write("<html><head><title>"+title+"</title></head></html>")
        self.f.write("<h1>"+title+"</h1>")
        self.makeTitleCalled = True

    def makeString(self, str):
        if not self.makeTitleCalled:
            raise RuntimeError
        self.f.write("<p>"+str+"</p>")

    def makeItems(self, items):
        if not self.makeTitleCalled:
            raise RuntimeError
        self.f.write("<ul>")
        for i in items:
            self.f.write("<li>"+i+"</li>")
        self.f.write("</ul>")

    def close(self):
        if not self.makeTitleCalled:
            raise RuntimeError
        self.f.write("</body></html>")
        self.f.close()

    def getResult(self):
        return self.filename
