"""
Python generators are a simple way of creating iterators.
a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
It is as easy as defining a normal function, but with a yield statement instead of a return statement.
The difference is that while a return statement terminates a function entirely, yield statement pauses the
function saving all its states and later continues from there on successive calls.

"""
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

##It returns an object but does not start execution immediately.
#a= my_gen()

# We can iterate through the items using next().
#print(next(a))
#print(a.__next__())
#print(next(a))

"""
Generator function contains one or more yield statements.
When called, it returns an object (iterator) but does not start execution immediately.
Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
Once the function yields, the function is paused and the control is transferred to the caller.
Local variables and their states are remembered between successive calls.
Finally, when the function terminates, StopIteration is raised automatically on further calls.

"""

# can also iterate using for loop
#print("printing using for loop")
#for item in my_gen():
#    print(item)


# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
#print(next(generator))
