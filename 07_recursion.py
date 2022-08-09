#finding factorial using loop
def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    return f

factorial_num =factorial(5)
print("factorial is ",factorial_num)

#finding factorial using recursion function.

def factorial_recursion(n):
    if n ==1:
        print(n)
        return 1
    else:
        print(n,"*",end="")
        return n*factorial_recursion(n-1)

print(factorial_recursion(5))