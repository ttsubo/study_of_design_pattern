from abc import ABCMeta, abstractmethod


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name
        self.__next = None

    def setNext(self, next):
        self.__next = next
        return next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif self.__next is not None:
            self.__next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return "[{0}]".format(self.__name)

    @abstractmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        print("{0} is resolved by {1}.".format(trouble, self))

    def fail(self, trouble):
        print("{0} cannot be resolved.".format(trouble))


class NoSupport(Support):
    def __init__(self, name):
        super(NoSupport, self).__init__(name)

    def resolve(self, trouble):
        return False


class LimitSupport(Support):
    def __init__(self, name, limit):
        super(LimitSupport, self).__init__(name)
        self.__limit = limit

    def resolve(self, trouble):
        return True if trouble.getNumber() < self.__limit else False


class OddSupport(Support):
    def __init__(self, name):
        super(OddSupport, self).__init__(name)

    def resolve(self, trouble):
        return True if trouble.getNumber() % 2 == 1 else False


class SpecialSupport(Support):
    def __init__(self, name, number):
        super(SpecialSupport, self).__init__(name)
        self.__number = number

    def resolve(self, trouble):
        return True if trouble.getNumber() == self.__number else False
