num = int(input("Enter the number: "))
temp = num
sum = 0

while num>0:
    dig = num % 10

    fact = 1
    for i in range (1, dig+1):
        fact = fact*i

    sum = sum + fact
    num = num //10

if (sum == temp):
    print('Strong number')
else :
    print("No strong number")
