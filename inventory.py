import pprint

inventory={
    'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12
}

def displayInv(inventory):
    print("the inventory list is: ")
    pprint.pprint(inventory)
    print("the total no. of items: ",sum(inventory.values()))

def addToInv(inventory):
    while True:
        inp1=input("Enter the new item(blank to exit): ")
        if inp1=='':
            displayInv(inventory)
            break
        inp2=int(input("Enter the no. of the item: "))
        inventory[inp1]=inp2

addToInv(inventory)