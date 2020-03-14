from mediator.mediator import Mediator


class Colleague(Mediator):
    def __init__(self, mediatorObj, name):
        self.mediator = mediatorObj
        self.name = name

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)


class ConcreteColleagueButton(Colleague):
    def __init__(self, mediatorObj, name=None):
        super(ConcreteColleagueButton, self).__init__(mediatorObj, name)
        self.active = False

    def clickButton(self):
        if self.active:
            self.on_change()
        return self.mediator.authentication

    def checkButtonStatus(self):
        return self.active


class ConcreteColleagueTextArea(Colleague):
    def __init__(self, mediatorObj, name=None):
        super(ConcreteColleagueTextArea, self).__init__(mediatorObj, name)
        self.text = None

    def inputText(self, text):
        self.text = text
        self.on_change()