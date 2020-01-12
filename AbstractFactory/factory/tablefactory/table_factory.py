from factory.factory import Factory, Link, Tray, Page


class TableFactory(Factory):
    def createLink(self, caption, url):
        return TableLink(caption, url)

    def createTray(self, caption):
        return TableTray(caption)

    def createPage(self, title, author):
        return TablePage(title, author)


class TableLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def makeHtml(self):
        return '<td><a href={}>{}</a></td>'.format(self.url, self.caption)


class TableTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def makeHtml(self):
        buf = []
        buf.append('<td>')
        buf.append('<table width="100%" border="1"><tr>')
        buf.append('<td bgcolor="#cccccc" algin="center" colsapn="{}"><b>{}</b></td>'.format(len(self.tray), self.caption))
        buf.append('</tr>\n')
        buf.append('<tr>\n')

        for item in self.tray:
            buf.append(item.makeHtml())

        buf.append('</tr></table>')
        buf.append('</td>')
        return ''.join(buf)


class TablePage(Page):
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
        buf.append('<table width="80%" border="3">\n')

        for item in self.content:
            buf.append('<tr>{}</tr>'.format(item.makeHtml()))

        buf.append('</table>')
        buf.append('<hr><adress>{}</adress>'.format(self.author))
        buf.append('</body>\n</html>\n')
        return ''.join(buf)
