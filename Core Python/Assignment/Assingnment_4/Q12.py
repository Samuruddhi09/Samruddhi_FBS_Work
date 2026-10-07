#12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

n = int(input("Enter n: "))

temp = n
sum = 0
count = 0

# Count number of digits
while temp > 0:
    count = count + 1
    temp = temp // 10

temp = n

# Find sum of powers of digits
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")