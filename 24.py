# The counter function counts down from start to stop when start is bigger than stop,
#  and counts up from start to stop otherwise.
#  Fill in the blanks to make this work correctly.
# def counter(start, stop):
# 	x = start
#     # tmp=""
# 	if start > stop:
# 		for x in range(start, stop, -1):
#             print(x)
	# else:
	# 	return_string = "Counting up: "
	# 	while x <= stop:
	# 		return_string += str(x)
	# 		if ___:
	# 			return_string += ","
	# 		___
	# return return_string

# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"
# counter(5,2)
def counter(start,stop):
    l=[]
    tmp=""
    if start>stop:
        for i in range(start,stop-1,-1):
            # print(i,end=',')
            l=i
            print(l)
    else:
        for i in range(start,stop+1):
            # print(i,end=',')
            l.append(i)
            # print(l)
        # print(l)
        
        print(tmp)

counter(1,10)
# counter(2,1)


