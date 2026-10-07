#1. WAP to print all even numbers until n.

n = int(input('Enter the Number: '))

for i in range (0,n+1):
    if (i%2 == 0):
        print (i)


# Enter the Number: 10
# 0
# 2
# 4
# 6
# 8
# 10