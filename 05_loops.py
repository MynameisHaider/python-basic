num=0
count=0
sum=0
name = input("enter your name")
print(name)

while num>=0:
   num=int(input("enter any number .. -1 to exit\n"))
   if num>=0:
       count=count+1 # this counts number of inputs
       sum=sum+num # this adds input number cumulatively.
avg=sum/count
print ("numbers input:",count, "average:",avg)