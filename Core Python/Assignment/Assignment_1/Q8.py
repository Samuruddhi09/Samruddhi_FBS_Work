# 8. Write a program to convert days into years, weeks and days.

num = int(input('Enter Total Number of Days: '))

years = num //365 

rd = num % 365

weeks = rd // 7

days = rd % 7

print(f'{num} is equals to {years}, {weeks}, {days}')

# Enter Total Number of Days: 12345
# 12345 is equals to 33, 42, 6