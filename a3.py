# Write a python program to find the largest of three numbers entered ny the user
a=int(input("Enter value of a:  "))
b=int(input("Enter value of b:  "))
c=int(input("Enter value of c:  "))
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print("Largest number is:   ",largest)    