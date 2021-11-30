# multiplication table using loops
i=1
while i<=10:
    print("5 x",i,"=",i*5)
    i+=1

n=int(input("Enter the table number: "))
for j in range(1,11):
    print(n,"x",j,"=",n*j)
