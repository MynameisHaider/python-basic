"""
#ITERATING STRING USING FOR LOOP
string = "computer"
for char in string:
    print(char)
"""

#iterating string using built in methods.
# it.__next__() = next(it) both are same
#It receives an iterable and returns iterator object.
"""
string = "wensam college"
it = iter(string)
while True:
    try:
        chr =next(it)
        print(chr)
    except StopIteration:
        break
"""

"""
CODE FROM W3 SCHOOL .COM
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
 Lists, tuples, dictionaries, strings and sets are all iterable objects.
"""
# define tuple or list
mytuple = ("apple", "banana", "cherry","mango")
#get an iterator using iter()
myit = iter(mytuple)

#print(myit.__next__())
# iterate through it using next() or .__next__() method
#rint(next(myit))
#print(next(myit))
#print(myit.__next__())

string = "lala is great"
string_iter = iter(string)
#print(next(string_iter))

for s in string_iter:
    print(s)