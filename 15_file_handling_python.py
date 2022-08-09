f = open("myfile.txt")
f2 = open("number.bin","wb")
#lines = f.read()
#lines = f.readlines()
#print(lines)

#using for loop
"""

for line in f:
    print(line)

"""
#content = f2.read()
#print(content)

#WRITING TO BINARY FILE
fbin=open("number.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)

fbin.write(arr)
fbin.close()

#f.close()
