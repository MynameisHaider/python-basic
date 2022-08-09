#EXCEPTION HANDLING
"""
Many a times though, program results in an error after it is run even if
it doesn’t have any syntax error. Such an error is a runtime error called as exception.
Two keywords -  try and except - perform exception handling.
The try: block contains statements which are susceptible for exception.
If block is executed without exception,
the except: block (which must appear immediately after try block) is SKIPPED.
IF THERE IS NO ERROR IN TRY, THEN EXCEPT PART WILL BE SKIPPED
"""
"""

marks={'Meena':50, 'Tina':60,'Leena':70}
name=input("enter name:")
try:
       print ('marks:',marks[name])
except KeyError:
       print ('name {} not in the list'.format(name))
print ("end of program")
"""
a=[10,20,30,40,50]
try:
       x=int(input('enter index: '))
       print ('number at index {} is {}'.format(x,a[x]))
except IndexError:
       print ("index is out of range")
except ValueError:
       print ("index should be an integer")