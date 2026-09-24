num = int(input('Enter Number: '))

if(num > 1):
    for i in range (2,num // 2+1):
        print(i)
        if (num % i == 0):
            print (f'{num} is not a Prime Number')

    else:
        print(f'{num} is a prime number')