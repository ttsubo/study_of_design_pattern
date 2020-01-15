from framework.manager import Manager
from framework.decoprototype.underline_pen_prototype import UnderlinePen
from framework.decoprototype.message_box_prototype import MessageBox


def startMain(managerObject):
    upen = UnderlinePen("-")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    managerObject.register("strong message", upen)
    managerObject.register("warning box", mbox)
    managerObject.register("slash box", sbox)

    p1 = managerObject.create("strong message")
    p2 = managerObject.create("warning box")
    p3 = managerObject.create("slash box")
    p1.use("Hello World")
    p2.use("Hello World")
    p3.use("Hello World")


if __name__ == "__main__":
    startMain(Manager())
