# Write a Python program to input a list of numbers and find the maximum and minimum values
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Maximum value:", maximum)
print("Minimum value:", minimum)
