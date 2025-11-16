# Enter number of students to register: 2

# Enter Student Name:
# Enter Student Regno:
# Enter Student phone:
# Enter Student email:
    
# Enter Student Name:
# Enter Student Regno:
# Enter Student phone:
# Enter Student email:
    
# Output
# student_records = {studentname:[],
#                    studentregno:[],
#                    studentphone:[],
#                    studentemail:[]}

print("************Student Registration**************")
studentnames = []
studentregno = []
studentphone = []
studentemail = []
students=int(input("Enter the number of students for register: "))
for i in range(students):
    student_name = input("Enter student name: ")
    student_regno = input("Enter student regno: ")
    student_phone = input("Enter student phone: ")
    student_email = input("Enter student email: ")
    studentnames.append(student_name)
    studentregno.append(student_regno)
    studentemail.append(student_email)
    studentphone.append(student_phone)
    print("---------student register done-----------")
else:
    print("All students registered.No of students registered: ",
          students)
students_records = {'studentnames': studentnames,
                    'studentregno': studentregno,
                    'studentemail': studentemail,
                    'studentphone': studentphone}
print(students_records)
# print(studentnames,studentemail,studentregno,studentphone)

# Enter the email: a
# Enter the password: 12
# Invalid email or password
# remaining attempts: 3

# Enter the email: abc
# Enter the password: 123
# login success

print("***********Student Login**************")
attempts = 3
while(True):
    eval = ""
    pval = ""
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    for i in students_records['studentemail']:
        if i == email:
            eval = "True"
            break
    for i in students_records['studentregno']:
        if i == password:
            pval = "True"
            break
    if(eval == "True" and pval == "True"):
        print("Login Success")
        break
    else:
        if(attempts == 0):
            print("All the attempts are over. Your username is blocked!")
            break
        attempts = attempts-1
        print("Invalid details")
        print("Remaining attempts: ",attempts)

# for i in range(2,10):
#     print(i)
# for j in range(10,20):
#     print(j)
