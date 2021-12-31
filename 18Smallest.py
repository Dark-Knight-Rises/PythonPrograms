l=[3,43,5,23,5,2,45,65,76,-1]
smallest=l[0]
for i in range(0,len(l)):
    if l[i]<smallest:
        smallest=l[i]
    
print("the smallest val is: ",smallest)

l.sort()
print(l)
print("smallest: ",l[0])
