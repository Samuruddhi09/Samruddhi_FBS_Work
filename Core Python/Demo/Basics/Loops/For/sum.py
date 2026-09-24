n = int(input('Enter the n: '))

sum = 0

for i in range(1, n+1):
    sum += i
    print (sum)

print (f'total sum {n} is {sum}')