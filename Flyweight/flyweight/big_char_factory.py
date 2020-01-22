class BigCharFactory(object):
    def __init__(self):
        self.__pool = {}

    @classmethod
    def getInstance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def getBigChar(self, charname):
        bc = self.__pool.get(charname)
        if bc is None:
            bc = BigChar(charname)
            self.__pool[charname] = bc
        return bc


class BigString(object):
    def __init__(self, string):
        self.bigchars = []
        self.factory = BigCharFactory.getInstance()
        for s in string:
            self.bigchars.append(self.factory.getBigChar(s))

    def print(self):
        for bc in self.bigchars:
            print(bc)


class BigChar(object):
    def __init__(self, charname):
        try:
            with open("big{0}.txt".format(charname), 'r') as txtfile:
                data = txtfile.read()
            self.__fontdata = data
        except IOError:
            self.__fontdata = charname + '?'

    def __str__(self):
        return self.__fontdata
