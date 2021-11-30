'''
Filename: d:\Programs\a\4.py
Path: d:\Programs\a
Created Date: Tuesday, November 30th 2021, 11:21:30 pm
Author: Piyush

Copyright (c) 2021 Your Company
'''

marks=int(input("Enter the marks: "))
res="fail"
if(marks>=90):
     res="O"
elif(marks>=80 and marks<90):
    res="A"
elif(marks>=70 and marks<80):
    res="B"
elif(marks>=60 and marks<70):
    res="C"
elif(marks>=50 and marks<60):
    res="D"
print("The result is: ",res)
    
    