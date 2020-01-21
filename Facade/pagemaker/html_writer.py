class HtmlWriter(object):
    def __init__(self, writer):
        self.writer = writer

    def title(self, title):
        self.writer.write("<html>\n")
        self.writer.write("<head>")
        self.writer.write("<title>{0}</title>".format(title))
        self.writer.write("</head>\n")
        self.writer.write("<body>\n")
        self.writer.write("<h1>{0}</h1>\n".format(title))

    def paragraph(self, msg):
        self.writer.write("<p>{0}</p>\n".format(msg))

    def link(self, href, caption):
        self.writer.write("<a href=\"{0}\">{1}</a>".format(href, caption))

    def mailto(self, mailaddr, username):
        self.link("mailto:{0}".format(mailaddr), username)

    def close(self):
        self.writer.write("</body>\n")
        self.writer.write("</html>\n")
        self.writer.close()
