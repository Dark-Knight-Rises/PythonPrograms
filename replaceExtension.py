'''
Given a list of filenames, we want to rename all the files with extension 
hpp to the extension h. To do this, we would like to generate a new list 
called newfilenames, consisting of the new filenames. Fill in the blanks in 
the code using any of the methods you’ve learned thus far, like a for loop 
or a list comprehension.
'''

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
def renameFiles(filenames):
    newfilenames=[]
    for fName in filenames:
        if fName.endswith("hpp"):
            newfilenames.append(fName.replace("hpp","h"))
        else:
            newfilenames.append(fName)
    return newfilenames
print(renameFiles(filenames)) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]