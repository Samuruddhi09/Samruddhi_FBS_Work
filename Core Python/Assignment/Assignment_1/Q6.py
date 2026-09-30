# 6. Write a Program to input two angles from user and find third angle of the triangle.

angle1 =int(input('Value of angle 1: '))
angle2 =int(input('Value of angle 2: '))

angle3 = 180- (angle1+angle2)

print(f'The value of remaining angle of triangle is {angle3} degree')

# Value of angle 1: 30
# Value of angle 2: 70
# The value of remaining angle of triangle is 80 degree