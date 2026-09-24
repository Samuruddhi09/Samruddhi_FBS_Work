n = int (input('How many Fibonacci number you want : '))

a = -1
b = 1

print (f'the fibonacci series for {n} is : ')
for i in range (n):
    c = a+b
    print (c ,end =" ")
    a = b
    b = c



