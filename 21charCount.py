import pprint

msg='It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for character in msg:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)