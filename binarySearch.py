import random

def binSrch(list,target):
    first=0
    last=len(list)-1
    while(first<=last):
        midPt=(first+last)//2
        if(list[midPt]==target):
            return midPt
        elif(list[midPt]<target):
            first=midPt+1
        elif(list[midPt]>target):
            last=midPt-1
    return None

def verify(mp):
    if mp!= None:
        print("The target is present at: ",mp)
    else:
        print("The target isn't present in the list ")

list=random.sample(range(1,100),50) #gen a lisy
# print(list)
list.sort() #sorting the list in asc order
print("The target value is: 10\tThe random sorted list is: \n",list)
res=binSrch(list,10)
verify(res)