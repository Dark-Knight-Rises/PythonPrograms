# factorial with recurssion
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

f=int(input("Enter a no. to cal factorial: "))
print("The factorial is: ",fact(f))