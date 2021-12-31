'''Taylor and Rory are hosting a party. They sent out invitations, and each
 one collected responses into dictionaries, with names of their friends and 
 how many guests each friend is bringing. Each dictionary is a partial list,
  but Rory's list has more current information about the number of guests. 
'''

def combine_guests(guests1, guests2):
    newDict={}
    # Combine both dictionaries into one, with each key listed 
    for k in guests2:
        newDict[k]=guests2.get(k)
    # only once, and the value from guests1 taking precedence
    for k in guests1:
        newDict[k]=guests1.get(k)
    return newDict

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
