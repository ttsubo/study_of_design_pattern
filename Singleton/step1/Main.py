class Singleton(object):
    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class Myclass(Singleton):
    def __init__(self, input):
        self.input = input


if __name__ == '__main__':
    one = Myclass(1)
    print("one.input={0}".format(one.input))
    two = Myclass(2)
    print("one.input={0}, two.input={1}".format(one.input, two.input))
    one.input = 0
    print("one.input={0}, two.input={1}".format(one.input, two.input))
