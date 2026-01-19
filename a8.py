''' Write a python program to reverse a 
given number and check whether it is a
palindriome'''
num=int(input("Enter a number...  "))
temp=num
rev=0
while num>0:
    digit = num%10
    rev=rev*10+digit
    num=num//10
    print("Reversed number...  ",rev)
    if temp==rev:
        print("Palindome number")
    else:
        print("Not a palindome number")