a = ('rahul','priya','kiran')
print(a)

a = list(a)
print(a)

a[-1] = 'Raj'
print(a)

a = tuple(a)
print(a)

a = [2,4,6,8,8,6,4,2]
print(list(set(a)))

# calculate area of circle by radius

radius = 20
area = 3.142*radius*radius
print(int(area))

# Reverse the following number without function

num = 123456789
numstr = str(num)
reversenum = numstr[::-1]
print(int(reversenum))