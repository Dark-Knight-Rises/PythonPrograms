# factorial with function
def factIt(num):
    pro=1
    for i in range(num):
        pro=pro*(i+1)
    return pro
p=factIt(5)
print("Factorial is: ",p)