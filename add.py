"""
{} is called placeholder. we can use name index {name}, number index {0}, or {} empty index
"""
def add(x, y):
   ttl=x+y
   print ("addition = {}".format(ttl))
   return


num1=int(input("Enter first number: "))

num2=int(input("Enter second number: "))
add(num1,num2)