import sys
import strategy.strategy
from strategy.strategy import WinningStrategy, CircularStrategy
from strategy.player import Player


def startMain():
    player1 = Player("Taro", WinningStrategy())
    player2 = Player("Hana", CircularStrategy())

    for _ in range(10000):
        nextHand1 = player1.nextHand()
        nextHand2 = player2.nextHand()
        if nextHand1.isStrongerThan(nextHand2):
            print("Winner:{0}".format(player1))
            player1.win()
            player2.lose()
        elif nextHand2.isStrongerThan(nextHand1):
            print("Winner:{0}".format(player2))
            player1.lose()
            player2.win()
        else:
            print("Even...")
            player1.even()
            player2.even()

    print("Total Result:")
    print(player1)
    print(player2)


if __name__ == '__main__':
    startMain()
