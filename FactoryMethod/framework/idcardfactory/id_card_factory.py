from framework.factory import Factory, Product


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def createProduct(self, owner):
        return IDCardProduct(owner)

    def registerProduct(self, product):
        self.owners.append(product.owner)


class IDCardProduct(Product):
    def __init__(self, owner):
        self.owner = owner
        print("I'll create {0}'s card".format(self.owner))

    def use(self):
        print("I'll use {0}'s card".format(self.owner))
