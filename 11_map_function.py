#MAP FUNCTION.
"""
Thebuilt-in  map() function is especially useful where it is required to process each item 
from one or more iterable sequences (string, list, tuple or dictionary). It subjects each element in the iterable to another function which may be either a built-in function, a lambda function or a user-defined function and returns the mapped object. 
The map() function needs two arguments:

map(Function, Sequence(s))
"""
from math import factorial
"""

print(factorial.__name__)
print(factorial.__module__)
print(factorial.__sizeof__)
print(factorial.__dir__)

"""

numbers = [1,2,3,4,5]
factmap = map(factorial,numbers)

#print("factorial using map function is ")
#print(list(factmap))


powermap = map(lambda x,y: x**y, [10,20,30],[1,2,3])
#print("power of numbers using lambda function")
#print(list(powermap))