import csv
"""
#list of dictionary
marks=[
{'name':'Seema', 'age':22, 'marks':45}, 
{'name':'Anil', 'age':21, 'marks':56},
{'name':'Mike', 'age':20, 'marks':60}
]

csvfile=open('information.csv','w', newline='')

fields=list(marks[0].keys()) #.keys() will use name, age and marks as a list/heading in information.csv file
obj=csv.DictWriter(csvfile, fieldnames=fields)     #The function takes fieldnames parameter which is a sequence of keys. 
obj.writeheader()      
obj.writerows(marks)      
csvfile.close() 
"""
#READING CSV FILE
csvfileread = open('information.csv', 'r', newline='')
objreader = csv.DictReader(csvfileread)
print(objreader.fieldnames) # heading of columns

for row in objreader:
    print(row)
csvfileread.close()