#functions

#user defined functions
#inbuilt functions
#anonymous function

class Continent:
    def __init__(self,size,no_of_countries,location,population):
        #assign values to variables
        self.size=size
        self.no_of_countries=no_of_countries
        self.location=location
        self.population=population

    #method
    def get_size_population(self):
        print("size is {} and population is {}".format(self.size,self.population))

africa=Continent(12000,55,'equator',3000000)
africa.get_size_population()

#modifying properties
africa.location="North Poll"
print(africa.location)

#deleting object
#del africa

#deleting a property
del africa.size


#inheritance

