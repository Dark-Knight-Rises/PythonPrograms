# reads a file from drive
f=open('test.txt','r')
data=f.read()
print(data)
f.close()

# to write in the file, file will be made if not present
f=open('another.txt','w')
f.write("Hello this is another file created by w mode")
f.close()

#append
f=open("another.txt",'a')
f.write("This statement is appended")
f.close()

# the WITH statement, context manger
# does not requires close statement

with open('another.txt') as f:
    print(f.read())