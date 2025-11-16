# Python variables

name = "Manoj"
age = 21
print(name)
print(age)
print(name,age)
print("My name is %s and my age is %s" %(name,age))

# Variable reassignment
print("-----------------------")

name = "priya"
age = 20
print(name)
print(age)
print(name,age)
print("My name is %s and my age is %s" %(name,age))

# Variables swapping
a= 20
b= 30
print(a,b)

#method 1:
temp = a # 20
a = b # 30
b = temp # 20
print(a,b)

#method 2:
a = 50
b = 60
print(a,b)
a,b = b,a
print(a,b)