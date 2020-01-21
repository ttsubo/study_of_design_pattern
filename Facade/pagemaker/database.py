from configparser import ConfigParser


class Database(object):
    @classmethod
    def getProperties(cls, dbname):
        filename = dbname + ".ini"
        conf = ConfigParser()
        try:
            conf.read(filename)
            return conf["MailAddress"]
        except Exception:
            print("Warning: [{0}] is not found.".format(filename))
