import sys
import time
from state.context import Context
from state.state import ConcreteStateBooting, ConcreteStateRun, ConcreteStateShutDown, ConcreteStateRestart


def setConcreteState(operation):
    if operation == "start":
        return ConcreteStateBooting("booting")
    elif operation == "stop":
        return ConcreteStateShutDown("shutdown")
    elif operation == "restart":
        return ConcreteStateRestart("restart")

def startMain(initial_operation, change_operation):
    obj = Context(setConcreteState(initial_operation))
    print("### パソコンを、[{0}]します".format(initial_operation))
    obj.handle()
    print("### パソコンは、[{0}]の動作状態になりました".format(obj.getState()))
    print("")

    print("... sleep 5 second")
    print("")
    time.sleep(5)

    obj.setState(setConcreteState(change_operation))
    print("### パソコンを、[{0}]します".format(change_operation))
    obj.handle()
    print("### パソコンの動作状態は、[{0}]になりました".format(obj.getState()))


if __name__ == "__main__":
    startMain(sys.argv[1], sys.argv[2])
