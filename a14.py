# Write a Python program to demonstrate user-defined functions by calculating the square and cube of a number.
# User-defined function to calculate square
def square(num):
    return num **2

# User-defined function to calculate cube
def cube(num):
    return num **3

# Input from the user
number = int(input("Enter a number: "))

# Function calls
sq = square(number)
cu = cube(number)

# Display results
print("Square of the number:", sq)
print("Cube of the number:", cu)
