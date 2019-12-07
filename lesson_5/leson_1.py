#List: collection of items that are ordered,changeable and indexed
shoppingList=['toothpaste','cake','pen']
#accessing items in a list
item0=shoppingList[0]
print(item0)

#list slicing
print(shoppingList[1:2])
print(type(shoppingList))

#changing item in a list
shoppingList[0] = 'book'
print(shoppingList)

#list length
print(len(shoppingList))

#List Methods
#append     .......adds an item to the end of the list
shoppingList.append('tooth paste')
print(shoppingList)

#insert()  .....adds an item into the list stating the index
shoppingList.insert(2,'milk')
print(shoppingList)
#pop() .....removes the last item in a list
shoppingList.pop()
print(shoppingList)

#del  .......deletes the whole list
todo=['eat','code','sleep','repeat']
print(todo)
#del todo
print(todo)

#clear ......removes items in a list
today=['eat','code','sleep','repeat' 'here']
print(today)
#clear(today)
print(today)

#checking if an itemexists in list
if 'cake' in shoppingList:
    print('cake is present in the list!')
else:
    print('cake is not in the list')
#extends .....adds more than one item in a list



#Dictionary:item collection that are unordered,indexed and changable

student={
    "age": "22",
    "height": "5.5",
    "eyeColor":"blue",
    "hairColor":"black",
    "yearOfBirth":"2000"
}
print(student)
print("the color of the student eyes is" + student["eyeColor"])

student["hairColor"]="red"
print(student)

print(student.get("height"))
#looping through dictionary
#using the values() function to return values of a dictionary
for x in student.values():
    print(x)


    for x in student:
        print(student[x])
#Looping through both keys and values, by using the items() function

for x,y in student.items():
    print(x,y)
#Tuple: item collection that are ordered and unchangable

#Set:item collection that are unordered and unchangabl

#variable name=['item1','item2','item3']





