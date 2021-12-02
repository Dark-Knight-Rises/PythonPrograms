import os
with open('test1.txt') as f:
    txt=f.read()
with open('test1Renamed.txt','w') as f:
    f.write(txt)
os.remove('test1.txt')