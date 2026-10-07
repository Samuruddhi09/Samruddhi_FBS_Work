#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3 digit number")
else:
    first = num // 100
    middle = (num // 10) % 10
    last = num % 10

    if first == last:
        print("Palindrome")
    else:
        print("Not palindrome")