import time
import random

def binS(list,target):
    first=0
    last=len(list)-1
    midPt=len(list)//2
    while first<=last:
        midPt=(first+last)//2
        if list[midPt]==target:
            return midPt
        elif list[midPt]<target:
            first=midPt+1
        elif list[midPt]>target:
            last=midPt-1
    return None

def linearSrch(list,target):
    start2=time.time()
    for i in range(0,len(list)):
        if(list[i]==target):
            return i
    # end2=time.time()
    # print("Time taken for Linear: ",end2-start2)
    return None

def verify(mp):
    if mp!= None:
        print("The target is present at: ",mp)
    else:
        print("The target isn't present in the list ")

list=random.sample(range(-10000,1000000),999999)
list.sort()
target=random.randint(-10000,100000)

start2=time.time()
res1=linearSrch(list,target)
print(f"The target value is: {target}\tThe random sorted list is:")
verify(res1)
end2=time.time()
print("Time taken for Linear: ",(end2-start2)/len(list))

print(f"The target value is: {target}\tThe random sorted list is:")
start1=time.time()
res=binS(list,target)
verify(res)
end1=time.time()
print("Time taken for binary: ",(end1-start1)/len(list))