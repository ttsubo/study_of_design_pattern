from mediator.mediator import Mediator


class Colleague(Mediator):
    def __init__(self, mediatorObj):
        self.mediator = mediatorObj

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)


class ConcreteColleagueButton(Colleague):
    def __init__(self, mediatorObj, name=""):
        super(ConcreteColleagueButton, self).__init__(mediatorObj)
        self.active = False
        self.name = name

    def clickButton(self):
        if self.active:
            self.on_change()
        return self.mediator.authentication

    def checkButtonStatus(self):
        return self.active


class ConcreteColleagueTextArea(Colleague):
    def __init__(self, mediatorObj, name=None):
        super(ConcreteColleagueTextArea, self).__init__(mediatorObj)
        self.name = name
        self.text = None

    def inputText(self, text):
        self.text = text
        self.on_change()