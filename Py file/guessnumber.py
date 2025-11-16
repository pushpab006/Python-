import random
res="true"
print("-------------------")
print("Guess Number Game")
print("-------------------")

number = random.randint(1,100)
# print(number)
score = 100
while(res=="true"):
    try:
        guessnum = int(input("Enter the guess number from 1 to 100: "))
        print("Your guess number: ",guessnum)
        if(guessnum > 100 or guessnum < 1):
            print("Enter number between 1 to 100")
            score = score-1
        elif(guessnum == number):
            print("Congratulations! You Won")
            print("Your Score: ",score)
            break
        elif(guessnum > number):
            print("Try Lower Number")
            score=score-1
        else:
            print("Try Higher Number")
            score=score-1
    except ValueError:
        print("Enter only numbers")
        score=score-1
