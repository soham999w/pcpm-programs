# Write a Python program to sort a list of numbers in ascending order.
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
numbers.sort()
print("Sorted list in ascending order:")
print(numbers)
