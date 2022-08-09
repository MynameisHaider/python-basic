"""
CSV FILE IN PYTHON.
USING 2ND METHOD.
FROM PROGRAMIZ WEBSITE
"""
import csv
"""
with open('information.csv','r') as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)

file.close() 
"""
# #We don't need to explicitly call the close() method. It is done internally when file is open using with() function.

#Then, the csv.reader() is used to read the file, which returns an iterable reader object.
#The reader object is then iterated using a for loop to print the contents of each row.

"""
#writing to file using .writer method
with open("cricketer.csv", "w") as file:
    writer =csv.writer(file) # can use delimiter = '\t' as argument in writer()
    writer.writerow(["SN","Name","Role"])
    writer.writerow([1,"Babar","Batsman"])
    writer.writerow([2,"Shaheen","Bowler"])
    writer.writerow([3,"Shadab","All Rounder"])
"""

#writing to file using .DictWriter method
"""
with open("cricketer.csv","w") as writetofile:
    fieldnames = ["SN","Name","Role"]
    writer =csv.DictWriter(writetofile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'SN': 1,'Name':"babar",'Role':"bat"})
    writer.writerow({'SN': 2,'Name':"haider",'Role':"bat"})
    writer.writerow({'SN': 3,'Name':"asif",'Role':"bat"})
    
    writer.writerow({'SN': 4,'Name':"inzi",'Role':"bat"})
    writer.writerow({'SN': 5,'Name':"lala",'Role':"bowl"})
    writer.writerow({'SN': 6,'Name':"akmal",'Role':"keeper"})
    writer.writerow({'SN': 7,'Name':"shafiq",'Role':"bat"})

"""


"""
with open("cricketer.csv","r") as readfile:
    reader1 =csv.DictReader(readfile)
    for row in reader1:
        print(row)  

"""
#using python library 
import pandas as pd
file=pd.read_csv("cricketer.csv")
print(file["Name"])