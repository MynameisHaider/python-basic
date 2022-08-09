import csv
#list of tuple
"""
marks=[('Seema',22,45),('Anil',21,56),('Mike',20,60)]
csvfile=open('marks.csv','w', newline='')
obj=csv.writer(csvfile)
for row in marks:
    obj.writerow(row)
"""

#READ CSV FILE
csvFileRead= open('marks.csv','r', newline='')
obj =csv.reader(csvFileRead)
for row in obj:
    print(row)

csvFileRead.close()

#csvfile.close()
