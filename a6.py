''' Write a python program to genrate 
the fibbonacci series up to n terms'''
num=int(input("Enter a number:  "))
a,b=0,1
print("Fibbonacci series:   ")
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b