birthday={'piyush': '10 jan', 'aditi':'4 june', 'manoj':'10 oct'}
while True:
    inp=input("enter a name: (blank to quit) ")
    if inp=='':
        break   
    if inp in birthday:
        print(f"{inp} has b'day on: {birthday[inp]}")
    else:
        print("i don't have the info for ",inp)
        inp2=input("Enter thier bday: ")
        birthday[inp]=inp2
        print("database updated.")
        