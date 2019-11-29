#operators: used to perform operations to variables and values

#Arithmetic
x=66
y=55.98
print("addition of {} and {} is {}".format(x,y,x+y))
print("subtraction of {} and {} is {}".format(x,y,x-y))
print("multiplication of {} and {} is {}".format(x,y,x*y))
print("division of {} and {} is {}".format(x,y,x/y))
print("modulus of {} and {} is {}".format(x,y,x%y))
print("Exponential of {} raised to {} is {}".format(3,2,3**2 ))

#calculate the are of a circle with radius 7

r=7
pie=3.14
area= r**2*pie
print(area)

#Assignment :used to assign a vaue to a variable
#1 =
name= "babra"
#2. +=
x=5
x=x+6
x+=6
print(x)

#comparison.....the result of a comparison operator always return boolean
#1.== equals

#2. !== not equal

#3.> < ,>=,<=


#Logical
""""and,
or,
not
........return value is boolean"""

x=3
y=2

print(x>y and x<9)
# and returns boolean true if both conditions are true and boolean false if one of the condition is false
print(x>y and x<1)

#or returns true if one of the conditions
print(x>y or x<1)

#nor returns true if a result is false
print(not(x>y and x<9))

#do research  on lists,tuple,sets,dict

#list
thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
