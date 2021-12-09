with open('auto.txt') as f:
    data=f.read()
words=data.split()

count={}
# print(data)
print("The list f words\n",words)
for i in words:
    count[i]=count.get(i,0)+1

print(count)