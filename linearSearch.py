def linearSrch(list,target,n):
    for i in range(0,n):
        if(list[i]==target):
            return i
    return None
def verify(i):
    if i is not None:
        print("The value is present at: ",i)
    else:
        print("The value isn't present")

l=[2,4,6,54,76,3,98]
n=len(l)
res=linearSrch(l,1,n)
verify(res)