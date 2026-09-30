#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

S1= int(input('Enter Marks for Subject 1: '))
S2= int(input('Enter Marks for Subject 2: '))
S3= int(input('Enter Marks for Subject 3: '))
S4= int(input('Enter Marks for Subject 4: '))
S5= int(input('Enter Marks for Subject 5: '))

total = S1+S2+S3+S4+S5

percentage = (total/500)*100 #Assuming that each subject's max marks is 100

print ('Percentage of student is: ', percentage)


# Enter Marks for Subject 1: 80
# Enter Marks for Subject 2: 65
# Enter Marks for Subject 3: 55
# Enter Marks for Subject 4: 90
# Enter Marks for Subject 5: 85
# Percentage of student is:  75.0