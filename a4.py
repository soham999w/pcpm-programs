# Write a python program to check whether a given year is a leap year
year=int(input("Enter a year of your choice:    "))
if(year % 4==0 and year % 100!=0) or(year % 400==0):
    print("Leap year...")
else:
    print("Not a Leap year...")