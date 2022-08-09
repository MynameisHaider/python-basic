#f = open("python.txt","a") # a for append, w for write, r for reading (by default)
#f.write("python is easy language to learn ")
#f.write("lets learn python for data science")
lines =[ "Beautiful is better than ugly.\n",
 "Explicit is better than implicit.\n",
  "Simple is better than complex.\n", 
  "Complex is better than complicated.\n"]
#f.writelines(lines)
f2 = open("python.txt","r") # open for reading.
print(f2.readlines())

f2.close()