# check if a word is present or not
with open('another.txt') as f:
    txt=f.read()
    if 'Hello' in txt:
        print("Present")
    else:
        print("Not present")
