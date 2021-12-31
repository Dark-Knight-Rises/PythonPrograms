import random
r=random.randint(1,10)
usr=None
guess=0
while(usr!=r):
    usr=int(input("enter The no: "))
    guess+=1
    if(usr==r):
        print("Congratulations you won! in ",guess,"turns")
    else:
        if(usr<r):
            print("Oops! guess higher")
        else:
            print("Oops! guess lower")
with open('guess.txt') as f:
    data=int(f.read())
    if(guess<data):
        print("Congratulations! you just broke your own highscore!")
        with open('guess.txt','w') as w:
            w.write(str(guess))

