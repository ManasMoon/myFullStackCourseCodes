# Write a program to find the greatest of four numbers entered by the user.


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if(a>b and a>c and a>d):
          print("a is greatest")
elif(b>a and b>c and b>d):
          print("b is greatest")
elif(c>a and c>b and c>d):
          print("c is greatest")
elif(d>a and d>b and d>c):
          print("d is greatest")
else:
          print("All numbers are equal")