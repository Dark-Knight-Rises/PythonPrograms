def max(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
    print(f"The numbers {n1},{n2} and {n3} are equal.")
    return None
n1=int(input("Enter the first no. "))
n2=int(input("Enter the sec no. "))
n3=int(input("Enter the third no. "))
print("The largest no. is: ",max(n1,n2,n3))