import time

def binS(list,target):
    if len(list) == 0:
        return False
    else:
        midPt=(len(list))//2
        if(list[midPt]==target):
            return True
        elif(list[midPt]<target):
            return binS(list[midPt+1:],target)
        else:
            return binS(list[:midPt-1],target)
    
def linearS(list,target):
    for i in range(0,len(list)):
        if list[i]==target:
            return True
    return False

l=list(range(-300000,300001,1))
target=300000
# print(l)
start=time.time()
res=linearS(l,target)
end=time.time()
leniarT=end-start
print(res," Linear Search\t Time taken: ",leniarT,"sec")

start=time.time()
res=binS(l,target)
end=time.time()
binT=end-start
print(res," Binary Search\t Time taken: ",binT,"sec")