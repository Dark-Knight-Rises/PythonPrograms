def format_name(first_name, last_name):
    # code goes here
    if (len(first_name) != 0 and len(last_name) != 0):
        string = "Name: " + last_name+", "+first_name
    elif(len(first_name) != 0 or len(last_name) != 0):
        string = "Name: "+first_name+last_name
        # return string
    else:
        string = ""
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

# Write a script that prints the multiples of 7 between 0 and 100.
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
for i in range(0, 101):
    if i % 7 == 0:
        print(i)
