class Hand(object):
    HANDVALUE_GUU = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2
    name = ["グー", "チョキ", "パー"]
    hands = []

    def __init__(self, handvalue):
        self.__handvalue = handvalue

    @classmethod
    def getHand(cls, handvalue):
        return cls.hands[handvalue]

    def isStrongerThan(self, hand):
        return self.fight(hand) == 1

    def isWeakerThan(self, hand):
        return self.fight(hand) == -1

    def fight(self, hand):
        if self == hand:
            return 0
        elif (self.__handvalue + 1) % 3 == hand.__handvalue:
            return 1
        else:
            return -1

#    def toString(self):
#        return self.name[self.__handvalue]


Hand.hands.append(Hand(Hand.HANDVALUE_GUU))
Hand.hands.append(Hand(Hand.HANDVALUE_CHO))
Hand.hands.append(Hand(Hand.HANDVALUE_PAA))