# if condition
# if-elif condition
# if-elif-else condition

# a = int(input("Enter the number"))
# if(a<5):
#     msg = "<5"
#     print(msg)
# elif(a>5):
#     msg = ">5"
#     print(msg)
# else:
#     msg = "=5"
#     print(msg)

# a = int(input("Enter the number 1: "))
# b = int(input("Enter the number 2: "))
# c = int(input("Enter the number 3: "))

# if(a>b and a>c):
#     print("a is greater")
# elif(b>a and b>c):
#     print("b is greater")
# else:
#     print("c is greater")
    

m1 = int(input("Enter the marks 1: "))
m2 = int(input("Enter the marks 2: "))
m3 = int(input("Enter the marks 3: "))
m4 = int(input("Enter the marks 4: "))
m5 = int(input("Enter the marks 5: "))
m6 = int(input("Enter the marks 6: "))

total = m1+m2+m3+m4+m5+m6
print("Total marks: ",total)
avg = total/6
print("Average marks: ",avg)

if(avg<=100 and avg>=85):
    print("Result: Distinction")
elif(avg<=84 and avg>=60):
    print("Result: First Class")
elif(avg<=59 and avg>=35):
    print("Result: Second class")
else:
    print("Result: Fail")
