"""
PASSING ARGUMENTS BY REFRENCE.
Python is a reference to the object in memory. both formal and actual arguments refer to same object.
therefor change in variable inside function will also make changes outside function.

"""
def append(list):
       list.append(60)
       print ("changed list inside function: ", list)
       return
numbers=[10,20,30,40,50]
print ("list before passing: ", numbers)
append(numbers)
print ("list after returning from function: ", numbers)