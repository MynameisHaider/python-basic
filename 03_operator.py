"""
OPERATION PERFORM ON SETS
"""
from re import A


set1 = {10,20,30,40,50}
set2 = {20,40,60}

#UNION
set3 = set1|set2
set_3 = set1.union(set2)
#print(sorted(set_3))
#print(type(set_3))

# INTERSECTION
set_4 = set1 & set2
#print(sorted(set_4))
#print(type(set_4))


"""
IDENTITY OPERATORS
is: returns true if both operands point to the same object and false otherwise.
is not: 	returns true if both operands don’t point to the same object and false otherwise.
"""
a =10
b = a # b act as reference to a
#print(id(a), id(b))
#print(a is b)

c = a*10 # now c is another variable
#print(c is a)

"""
BITWISE OPERATORS
& Binary AND
| Binary OR
^ Binary XOR
~  	Binary Ones Complement : It is unary operator that flips bits.
<< Binary Left Shift. bits moved to left by specified places and adds trailing 0s
>> Binary Right Shift. 	bits moved to right by specified places and adds leading 0s

"""

a1,b1 = 45,25
print(bin(a1), bin(b1))

#binary AND
c1 = a1 & b1
print(c1, bin(c1))

##binary complement
c2 = ~a1
print(c2, bin(c2))