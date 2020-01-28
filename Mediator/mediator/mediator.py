from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def on_change(self, component):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self.authentication = False

    def setColleagues(self, inputIdObj, inputPwObj, buttonObj):
        self.inputIdObj = inputIdObj
        self.inputPwObj = inputPwObj
        self.buttonObj = buttonObj

    def on_change(self, component):
        if component.name == "ID" or component.name == "PW":
            self.__refreshButton()
        elif component.name == "Login":
            self.__authentication()

    def __refreshButton(self):
        if self.inputIdObj.text is not None and self.inputPwObj.text is not None:
            print("(Active login button)")
            self.buttonObj.active = True

    def __authentication(self):
        if self.inputIdObj.text == "hoge" and self.inputPwObj.text == "fuga":
            print("(ID/PW is confirmed)")
            self.authentication = True
        else:
            print("(ID/PW is incorrect)")
