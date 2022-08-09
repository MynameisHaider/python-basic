f = open("myfile.txt","a")
lines =["this is fifth line written by using file object\n"]
#writing to file using append method
f.writelines(lines)

#reading file using exception handling
try:
    f = open("myfile.txt","r")
    while True:
        line=f.readline()
        if line =="":break
        print(line,end="")
except FileNotFoundError:
    print("file does not exits")
else:
    f.close()
