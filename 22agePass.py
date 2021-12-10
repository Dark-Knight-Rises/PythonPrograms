def setAge():
    while True:
        print("Enter your age integer only: ")
        age=input()
        if age.isdecimal():
            setPass()
            break
        print("not an int!\n")

def setPass():
    while True:
        print("enter the pass, in alphanumeric: ")
        psw=input()
        if psw.isalnum():
            break
        print("try again!\n")

setAge()