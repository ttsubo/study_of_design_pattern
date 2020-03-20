from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass

class ConcreteState(State):
    def __init__(self, state):
        self.state = state
    
    def getConcreateState(self):
        return self.state


class ConcreteStateBooting(ConcreteState):
    def __init__(self, state):
        super(ConcreteStateBooting, self).__init__(state)

    def handle(self, context):
        print("*** パソコンは、起動中です")
        context.setState(ConcreteStateRun("running"))


class ConcreteStateRun(ConcreteState):
    def __init__(self, state):
        super(ConcreteStateRun, self).__init__(state)

    def handle(self, context):
        print("*** パソコンは、動作中です")


class ConcreteStateShutDown(ConcreteState):
    def __init__(self, state):
        super(ConcreteStateShutDown, self).__init__(state)

    def handle(self, context):
        print("*** パソコンは、停止しています")


class ConcreteStateRestart(ConcreteState):
    def __init__(self, state):
        super(ConcreteStateRestart, self).__init__(state)

    def handle(self, context):
        print("*** パソコンは、再起動をはじめます")
        context.setState(ConcreteStateBooting("booting"))
        context.handle()
