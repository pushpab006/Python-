# Types of Data types:

# 1. int
# 2. float
# 3. string
# 4. boolean
# 5. list
# 6. tuple
# 7. dictionary
# 8. sets


a = 20 
b = -1

print(type(a))
print(type(b))

a = 2.5
b = -1.5

print(type(a))
print(type(b))

a = "Hello"
b = 'World'
print(type(a))
print(type(b))

a = True
c = False
print(type(a))
print(type(c))

#       0     1   2
a = ["Manoj",23,False]
print(a,type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[-1])

a[2] = True
print(a)

a = [['mohan','abhi','raju'],[22,32,34],[False,True,True]]
print(a)
print(len(a))

# mohan 22 False
# abhi  32 True
# raju  34 True

print(a[0][0],a[1][0],a[2][0])

a = ('apple','banana','mango','orange')
print(a,type(a))

print(a[0])
print(a[-1])

# a[1] = 'chickoo'

a= (['raj','preeti','kiran'],[20,21,22])
print(a)
print(a[0],a[1])
a[0][0] = 'mohan'
print(a)

# Dictionary

a = {1: 'mumbai', 2: 'delhi', 3:'bengaluru'}
print(a,type(a))

a = {'city': ['mumbai', 'delhi', 'bengaluru'],
     'place':['Gateway of India','India Gate','Lalbagh']}
print(a)

print(a['city'][0],a['place'][0])
print(a['city'][1],a['place'][1])
print(a['city'][2],a['place'][2])


a = {1,2,3,4,5}
print(a,type(a))

a = {1,2,3,4,5,5,4,3,2,1}
print(a)

# print(a[0])