'''
Filename: d:\Programs\a\path.py
Path: d:\Programs\a
Created Date: Saturday, December 11th 2021, 7:27:56 pm
Author: Piyush

Copyright (c) 2021 Your Company
'''
with open('auto.txt') as f:
    data=f.read()

di=dict()
data=data.rstrip()
wds=data.split()
print("\nList\n",wds)
for w in wds:
    di[w]=di.get(w,0)+1

tmp=list()
for k,v in di.items():
    newt=(v,k)
    tmp.append(newt)
tmp=sorted(tmp,reverse=True)
print("Sorted")
for v,k in tmp[:5]:
    print(k,v)