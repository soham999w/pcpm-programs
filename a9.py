# write a python program to sum of digit of given number
num = int(input("Enter a number: "))
num = abs(num)
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Sum of digits:", sum_of_digits)
