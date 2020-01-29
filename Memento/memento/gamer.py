import random
from memento.memento import Memento


class Gamer(object):
    def __init__(self, money):
        self.__fruitname = ["リンゴ", "ぶどう", "バナナ", "みかん"]
        self.__money = money
        self.__fruits = []

    def getMoney(self):
        return self.__money

    def bet(self):
        dice = random.randint(1, 6)
        if dice == 1:
            self.__money += 100
            print("所持金が増えました")
        elif dice == 2:
            self.__money //= 2
            print("所持金が半分になりました")
        elif dice == 6:
            f = self.__getFruit()
            print("フルーツ({0})をもらいました".format(f))
            self.__fruits.append(f)
        else:
            print("何も起こりませんでした")

    def createMemento(self):
        m = Memento(self.__money)
        for f in self.__fruits:
            if f.startswith("おいしい"):
                m.addFruit(f)
        return m

    def restoreMemento(self, memento):
        self.__money = memento.money
        self.__fruits = memento.getFruits()

    def __str__(self):
        return "[money = {0}, fruits = {1}]".format(self.__money, self.__fruits)

    def __getFruit(self):
        prefix = ''
        if bool(random.getrandbits(1)):
            prefix = "おいしい"
        return prefix + random.choice(self.__fruitname)
