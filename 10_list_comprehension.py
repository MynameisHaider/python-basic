#LIST COMPREHENSION
"""
List comprehension techniques follow mathematical set builder notation. It is a very concise and 
efficient mechanism of creating new list by performing a certain process on each item of existing list. 
List comprehension is considerably efficient than processing a list by for loop
"""
squares=[]
for num in range(6):
        squares.append(pow(num,2))
print (squares)

#The same list can be created by using list comprehension instead of using for loop

squares_1 = [x*x for x in range(6)] #list comprehension
print(squares_1)

#DICTIONARY COMPREHENSION
dictionary = [{x:x*10} for x in range(1,6)]
print("dictionary comprehension is: ", dictionary)