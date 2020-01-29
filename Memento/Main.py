import time
from memento.gamer import Gamer


def startMain():
    gamer = Gamer(100)
    memento = gamer.createMemento()

    for i in range(100):
        print("==== {0}".format(i))
        print("現状:{0}".format(gamer))
        gamer.bet()
        print("所持金は{0}円になりました".format(gamer.getMoney()))

        if gamer.getMoney() > memento.getMoney():
            print("      (だいぶ増えたので、現在の状態を保存しておこう)")
            memento = gamer.createMemento()
        elif gamer.getMoney() < memento.getMoney() / 2:
            print("      (だいぶ減ったので、以前の状態に復帰しよう)")
            gamer.restoreMemento(memento)

        time.sleep(1)
        print("")


if __name__ == '__main__':
    startMain()
