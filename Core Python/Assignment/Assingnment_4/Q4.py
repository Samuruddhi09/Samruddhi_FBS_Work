# 4. WAP to print factorial of a number .
n = int(input('Enter value for n: '))

fact = 1

for i in range (1,n+1):
    fact *=i

print(fact)

# Enter value for n: 3
# 6