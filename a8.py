''' Write a python program to reverse a 
given number and check whether it is a
palindriome'''
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed number:", reversed_num)
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
