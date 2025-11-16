try:
    data = open("data.txt","w")
    data.write("Good morning\nHow are you?\nHave a good day!")
    print("File created!")
    
    data = open("data.txt","r")
    content = data.read()
    print(content)
    
    # shuffles pointer to top
    data.seek(0)
    
    print("-----------------")
    
    content = data.readline()
    print(content)
    
    # shuffles pointer to top
    data.seek(0)
    
    print("-----------------")
    
    content = data.readlines()
    print(content)
    
except FileNotFoundError:
    print("File not found in current folder")
finally:
    data.close()
    
print("-------Docx Reading--------")

import docx
def read_doc(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

file_path = "credit.docx"
content = read_doc(file_path)
print(content)


import pandas as pd

data = pd.read_csv("carsales.csv")
print(data)
makes = data['Make'] 
colors = data['Colour']
odometer = data['Odometer']
doors = data['Doors']
price = data['Price']

print(makes,colors,odometer,doors,price)

sales = data["Sales"]
totalsales = sales.sum()
print(totalsales)

print(data.dtypes)
print(data["Price"].sum())