num = 145

sum = 0
org = num

for dig in str(num):
    dig = int (dig)

    fact = 1
    for i in range (1, dig + 1):
        fact *= i

    sum += fact

if (sum == org):
    print('Strong number')
else :
    print("No strong number")

