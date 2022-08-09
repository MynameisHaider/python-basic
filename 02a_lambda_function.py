from numpy import double


"""
LAMBDA OR ANONYMOUS FUNCTION
anonymous functions are defined using the lambda keyword.
can have multiple arguments but only one expression.


"""

#double = lambda x:x*2

# here x is argument and x*2 is expression
#This function has no name. It returns a function object which is assigned to the identifier double. 
# We can now call it as a normal function
#print(double(5))
"""
In Python, we generally use it as an argument to a higher-order function (a function that
takes in other functions as arguments). 
Lambda functions are used along with built-in functions like filter(), map() etc.

"""

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

#map() takes a function and a list as arguments
new_list = list(map(lambda x: x * 2 , my_list)) # we need to convert the result into list()

#print(new_list)

"""
CODE FROM GEEKFORGEEK
"""
tables = [lambda x=x: x*10 for x in range(1, 11)]
 
#for table in tables:
 #   print(table())  

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
#print(uppered_animals)

from functools import reduce
li = [5, 8, 10, 20, 50, 100,7]
sum = reduce((lambda x, y: x + y), li)
print (sum)
# Here the results of the previous two elements are added to the next element and this goes on
#  till the end of the list like (((((5+8)+10)+20)+50)+100)+7)).