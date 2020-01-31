from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateBooting(State):
    def handle(self, context):
        print("*** パソコンは、起動中です")
        context.setState(ConcreteStateRun())


class ConcreteStateRun(State):
    def handle(self, context):
        print("*** パソコンは、動作中です")


class ConcreteStateShutDown(State):
    def handle(self, context):
        print("*** パソコンは、停止しています")


class ConcreteStateRestart(State):
    def handle(self, context):
        print("*** パソコンは、再起動をはじめます")
        context.setState(ConcreteStateBooting())
        context.handle()
