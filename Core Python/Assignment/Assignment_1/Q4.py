#4. Write a program to enter P, T, R and calculate simple Interest.

P = int (input('Enter the principal amount: '))
R = int (input('Enter the Rate of intrest: '))
T = int (input('Enter the Time Period: '))

SI = (P*R*T)/100

print(f'Your Simple intrest is {SI}')


# Enter the principal amount: 10000
# Enter the Rate of intrest: 5
# Enter the Time Period: 1
# Your Simple intrest is 500.0