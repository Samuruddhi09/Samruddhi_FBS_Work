# 7. Program to Find the Roots of a Quadratic Equation

print('equation in format ax^2 + bx + c = 0')

a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))

D = (b**2) - 4*a*c

x1= (-b+D**0.5)/(2*a)
x2= (-b-D**0.5)/(2*a)

print(f'Root of equation {a}x^2 + {b}x + {c} = 0 is {x1}, {x2}')

# equation in format ax^2 + bx + c = 0
# Value of a: 1
# Value of b: -5
# Value of c: 6
# Root of equation 1x^2 + -5x + 6 = 0 is 3.0, 2.0