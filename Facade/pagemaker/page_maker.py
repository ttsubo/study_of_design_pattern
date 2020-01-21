import sys
import json
from pagemaker.database import Database
from pagemaker.html_writer import HtmlWriter


class PageMaker(object):
    @classmethod
    def makeWelcomePage(cls, mailaddr, filename):
        try:
            prop = Database.getProperties('maildata')
            username =prop[mailaddr]
            writer = HtmlWriter(open(filename, 'w'))
            writer.title('Welcom to {}s page!'.format(username))
            writer.paragraph("We'll wait for your sending")
            writer.mailto(mailaddr, username)
            writer.close()
            print('{} is created for {} ({})'.format(filename, mailaddr, username))
        except Exception:
            print("# Failure occurred")
