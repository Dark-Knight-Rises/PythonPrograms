'''
Question 3
A professor with two assistants, Jamie and Drew, wants an attendance list of 
the students, in the order that they arrived in the classroom. Drew was the 
first one to note which students arrived, and then Jamie took over. After 
the class, they each entered their lists into the computer and emailed them 
to the professor, who needs to combine them into one, in the order of each 
student's arrival. Jamie emailed a follow-up, saying that her list is in 
reverse order. 
'''

def combine_lists(list1, list2):
    newList=list2+list1[::-1]
    return newList
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
