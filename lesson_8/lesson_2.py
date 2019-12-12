#inheritance
class Animal:#parent class
    def __init__(self,name,country):
        self.name=name
        self.country=country

    def printDetails(self):
        print("The name is :{} and country of origin is:{}".format(self.name,self.country))

class Goat(Animal):#child class
    #pass #used when you dont want to add any code
    def __init__(self,name,country,owner): #the child will no longer inherit parent's
        self.name=name
        self.country=country
        self.owner=owner
    def printDetails(self):
        print("The name is :{} and country of origin is:{} ,the owner is {}".format(self.name,self.country,self.owner))


#object
g1=Goat("gush","kenya" ,"jon")
g1.printDetails()

g2=Goat("brayo","sudan",'doe')
g2.printDetails()

class Dog(Animal):
    def __init__(self,name,country,color):
        # Animal.__init__(self,name,country) #for a child to inherit from the parent class 'animal'
        # inhert from parent
        super().__init__(name,country)
        self.color=color
    def printDetails(self):
        print("name: {} and country : {} and the color is:{}".format(self.name,self.country,self.color))

d1=Dog('smooth',"chiwawa","red")
d1.printDetails()