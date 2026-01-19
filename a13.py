# Write a Python program to perform linear search on a list.
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)
search_element = int(input("Enter the element to search: "))
found = False
for i in range(n):
    if numbers[i] == search_element:
        print(f"Element found at position {i + 1}")
        found = True
        break

if not found:
    print("Element not found in the list")
