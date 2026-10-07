#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
else:
    print('No number found')

#Enter n: 10
# No number found
# Enter n: 100
# 35
# 70
# No number found