#9. WAP to print all numbers in a range divisible by a given number.
n = int(input("Enter n: "))
num = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i % num == 0:
        print(i)

# Enter n: 20
# Enter the number: 5
# 5
# 10
# 15
# 20