# sum of first n terms with recursion
def sumAll(n):
    if(n==1):
        return 1
    return n+sumAll(n-1)
n1=int(input("Enter the no. for first n terms: "))
print("The sum is: ",sumAll(n1))