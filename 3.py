# Check the greatest no
num1=int(input("Enter 1st "))
num2=int(input("Enter 2st "))
num3=int(input("Enter 3st "))
num4=int(input("Enter 4st "))
f1=num2
f2=num4
if(num1>num2):
    f1=num1
if(num3>num4):
    f2=num3
if(f1>f2):
    print("The greatest no is ",f1)
else:
    print("The greatest no is ",f2)

    