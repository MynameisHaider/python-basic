#ELSE AND FINNALY IN EXCEPTION
"""

x=0
try:
   x=int(input("enter number: "))
except ValueError:
   print("ValueError raised")
else:
   print(x)
finally:
   x=0
   print ("reset x to ",x )
"""

"""
The finally block is typically employed to perform some kind of cleaning up operations in a process. 
For example you must close a file irrespective of errors in read/write operations.
"""
#assert statement
"""
The assert keyword checks whether given expression is true or false. Program execution terminates if it is false
by raising AssertionError and proceeds only if the expression is true
"""
num=int(input('enter marks [out of 100] : '))
assert num>=0 and num<=100, "DISPLAY YOUR ERROR MESSAGE HERE"
print ('marks obtained: ', num)