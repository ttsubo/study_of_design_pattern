from factory.factory import Factory, Link, Tray, Page


class ListFactory(Factory):
    def createLink(self, caption, url):
        return ListLink(caption, url)

    def createTray(self, caption):
        return ListTray(caption)

    def createPage(self, title, author):
        return ListPage(title, author)


class ListLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def makeHtml(self):
        return '  <li><a href="{}">{}</a></li>\n'.format(self.url, self.caption)


class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def makeHtml(self):
        buf = []
        buf.append('<li>\n')
        buf.append(self.caption + '\n')
        buf.append('<ul>\n')

        for item in self.tray:
            buf.append(item.makeHtml())

        buf.append('</ul>\n')
        buf.append('</li>\n')
        return ''.join(buf)


class ListPage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def makeHtml(self):
        buf = []
        buf.append('''
<html>
  <head><title>{}</title></head>
'''.format(self.title))
        buf.append('<body>\n')
        buf.append('<h1>{}</h1>'.format(self.title))
        buf.append('<ul>')

        for item in self.content:
            buf.append(item.makeHtml())

        buf.append('</ul>')
        buf.append('<hr><adress>{}</adress>'.format(self.author))
        buf.append('</body>\n</html>\n')
        return ''.join(buf)
