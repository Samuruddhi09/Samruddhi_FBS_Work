num = 432

d1 = num % 10 #2
print (d1) 
num1 = num // 10 #43

d2 = num1 % 10 #3
print (d2)
num2 = num1 //10 #4

d3 = num2 % 10 #4
print(d3)

num3 = num2 //10 #0
print (num3)

print (f'the seprated numbers are {d3} ,{d2}, {d1} and atlast the value of num is {num3}')