import json

#open fie
data= json.load(open("data.json"))

#function to find existing words
def translate(word):
#converting everything to a lower case value
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please check it."

word = input("Enter word:")
print(translate(word))
