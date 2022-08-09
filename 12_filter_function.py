# FILTER FUNCTION
"""
The filter() function also receives two arguments, a function with Boolean return value and a sequence.
Only the items for which the function returns True are stored in a filter object
"""
from asyncio import constants
print(constants.__name__)


def isVovel(x):
    for char in x:
        if char in ['a','e','i','o','u']:
            return False
    else:
        return True


string = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
'''
constants =list(filter(isVovel,string))
print("the new sequence without vovels is ")
#print(constants)
#print("".join(constants))

#USING LAMBDA FUNCTION WITH FILTER METHOD
consonants_1=list(filter(lambda x: x not in ['a','e','i','o','u'],string))
#print (''.join(consonants_1))