'''
The syntax of a lambda expression is as follows:
lambda <parameter_list>: <expression>
lambda function is used for one time use
The value of a lambda expression is a callable function, 
just like a function defined with the def keyword. It takes arguments, 
as specified by <parameter_list>, and returns a value, as indicated by <expression>.

A lambda function can take any number of arguments, but can only have one expression.

'''



from audioop import reverse


def reverse(s):
    return s[::-1] #slicing of string

print(reverse("i am a string"))


reverse_lambda = lambda s: s[::-1]
print(reverse_lambda("i am lambda string"))
#print(callable(lambda s: s[::-1]))

'''
The built-in Python function callable() returns True 
if the argument passed to it appears to be callable and False otherwise.
'''
