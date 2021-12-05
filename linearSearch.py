import random
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

list=random.sample(range(1,100),50)
# l=[2,4,6,54,76,3,98]
print("We want to find 10\tThe list of 50 values chosen at random is:\n",list)
n=len(list)
res=linearSrch(list,10,n)
verify(res)