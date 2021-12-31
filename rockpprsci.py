# game of rock paper scissors between you and computer
import random
def comp():
    r=random.randint(1,3)
    c='s'
    if(r==1):
        c='r'
    elif(r==2):
        c='p'
    return c
def winGame(comp,you):
    if(comp==you):
        return None
    elif(comp=='r'):
        if(you=='p'):
            return True
        return False
    elif(comp=='p'):
        if(you=='r'):
            return False
        return True
    elif(comp=='s'):
        if(you=='r'):
            return True
        return False
you=input("Enter rock(r) paper(p) or scisscors(s): ")
ch=comp()
print("The computer chose: ",ch,"You chose: ",you)
print("Our winner is: ")
s=winGame(ch,you)
if s:
    print("You!")
elif s==None:
    print("Its a tie")
else:
    print("The computer won!")