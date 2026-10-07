#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))
m4 = float(input("Enter subject 4 marks: "))
m5 = float(input("Enter subject 5 marks: "))

percentage = (m1 + m2 + m3 + m4 + m5) / 5

print("Percentage =", percentage)

if percentage >= 75:
    print("Distinction")
elif percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 35:
    print("Pass")
else:
    print("Fail")