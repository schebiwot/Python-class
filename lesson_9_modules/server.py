import thisisthefiletotest as test
import os
import platform

#use the dot operator to access properties in a module by mentioning the class imported
newList = test.shopping_list
newDict = test.myDict
classObj = test.Town('Nairobi')

#accessing name from the dictionary
name= newDict['name']
print(name)


print(newList)
print(newList[0])

print(newDict)
print(newDict['name'])


#accessing a class from another file
classObj.getName()

#accessing function from another file
newFunction = test.getDetails(newList,name)

mysys=platform.system()
print(mysys)

name = input("enter the name of your dog")
print(name)


# file handling
# try ...except finally
# JSON,regex,pip(python index ,,,),Dates,iterators,lambda(fxn without a name),list_comprehension