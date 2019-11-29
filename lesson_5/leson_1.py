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
del todo
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

#Tuple: item collection that are ordered and unchangable

#Set:item collection that are unordered and unchangable

#variable name=['item1','item2','item3']



