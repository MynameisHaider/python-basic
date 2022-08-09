#FILE OBJECT AS ITERATOR
f=open("python.txt","r")
while True:
       try:
               line=next(f)
               print (line, end="") #end each line with space
       except StopIteration:
               break
f.close()