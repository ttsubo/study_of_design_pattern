class Memento(object):
    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def addFruit(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return self.fruits
