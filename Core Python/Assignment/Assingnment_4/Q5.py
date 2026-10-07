#5. WAP to print Fibonacci series upto n.

n = int(input('Enter value for n: '))

a = -1
b = 1

for i in range (n):
    c = a + b
    print (c ,end=' ')

    a=b
    b=c


#Enter value for n: 10 
#0 1 1 2 3 5 8 13 21 34 