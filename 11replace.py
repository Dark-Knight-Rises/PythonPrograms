with open('another.txt') as f:
    contents=f.read()
contents=contents.replace('Hello','replacedHello')
with open('another.txt','w') as f:
    f.write(contents)