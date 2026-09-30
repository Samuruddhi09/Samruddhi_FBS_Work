# 5. Write a program to enter P, T, R and calculate Compound Interest.

P = int (input('Enter the principal amount: '))
R = int (input('Enter the Rate of intrest: '))
T = int (input('Enter the Time Period: '))

amount = P*(1+R/100)**T

CI = amount - P

print(CI)


# Enter the principal amount: 10000
# Enter the Rate of intrest: 5
# Enter the Time Period: 1
# 500.0