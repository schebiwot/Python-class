shopping_list=['rice','beef','cooking oil']#list
myDict= {
    "name": "John",
    "amount":  1200,
    "shop": "Naivas"

}

class Town:
    def __init__(self,name):
        self.name=name

    def getName(self):
        print("{} supermarket".format(self.name))


def getDetails(shoppingList,customer):
    print("{} shopping list bought by :{}".format(shoppingList,customer))

