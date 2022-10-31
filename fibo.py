#A Program to Display Fibonacci Sequence Using Recursion.
def fibo(n):
    if(n <= 1):
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
def fiboSequence(n):
    f = []
    for i in range(n):
        f.append(fibo(i))
    return f
n = int(input("enter n for getting first n numbers \n"))
fib = fiboSequence(n)
print("First n Fibonacci numbers are")
for i in fib:
    print(i , end = " ")
print("")
