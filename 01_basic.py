'''
CHECK THESE OUT
PYTHON DECORATOR ?
CALL BACK ?
LAMBDA EXPRESSION ?
SORTED() VS SORT() ?
ARGUMENT VS PARAMETER

'''


def fun():
    print('i am function')

#print(fun())
#print(id(fun))
#rint("cat",fun(),43)

#objects = ["cat",fun(),43]
#print(objects[1])
#print(objects[1])

#2 FUNCTION COMPOSITION
#passing function inside a function.
#python allow it in FUNCTIONAL PROGRAMMING.

def inner():
    print("i am inner function")

def outer(function):
    print(function())

'''
When you pass a function to another function, the passed-in function
sometimes is referred to as a callback because a call back to the inner function 
can modify the outer function’s behavior.'''
print(outer(inner)) 
#passing function as argument. 
#then outer will access to function called inner, and will print required result