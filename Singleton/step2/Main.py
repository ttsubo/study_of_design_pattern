class Singleton(object):
    @classmethod
    def get_instance(cls, input):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance

class Myclass(Singleton):
    def __init__(self, input):
        self.input = input

if __name__ == '__main__':
    one = Myclass.get_instance(1)
    print("one.input={0}".format(one.input))
    two = Myclass.get_instance(2)
    print("one.input={0}, two.input={1}".format(one.input, two.input))
    one.input = 0
    print("one.input={0}, two.input={1}".format(one.input, two.input))
