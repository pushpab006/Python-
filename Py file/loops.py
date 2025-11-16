# num = int(input("Enter the number"))
# bnum = int(input("Enter the birth number"))
# i = 2
# while(i<=num):
#     if(i%bnum == 0):
#         print(i," The number is lucky")
#         i= i+2
#     else:
#         print(i)
#         i = i+2

# print("-----odd numbers-------")     
# n = int(input("Enter the number: "))   
# for i in range(1,n,2):
#     print(i)
# else:
#     print("End of odd numbers")

# print("-----even numbers-------")     
# n = int(input("Enter the number: "))   
# for i in range(2,n,2):
#     print(i)
# else:
#     print("End of even numbers")


# n = int(input("Enter the number: "))
# evenlist = []
# oddlist = []
# squarelist = []
# cubelist = []
# for i in range(1,n):
#     if(i%2==0):
#         square = i*i
#         evenlist.append(i)
#         squarelist.append(square)
#     else:
#         cube = i*i*i
#         oddlist.append(i)
#         cubelist.append(cube)
# print("Even numbers: ")
# print(evenlist)
# print("Square numbers: ")
# print(squarelist)
# print("Odd numbers: ")
# print(oddlist)
# print("Cube numbers: ")
# print(cubelist)

search = input("Enter the fruit to be searched: ")
fruits = ['mango','banana','orange','watermelon']
result = ""
for i in fruits:
    if(i == search):
        result = search + " found"
        break
    else:
        result = search + " not found"
print(result)
