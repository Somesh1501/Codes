n = int(input())
def fibbonaci(n):
    fib = []
    i=1
    if n == 0:
        fib = []
    elif n == 1:
        fib =[1]
    elif n == 2:
        fib = [1,1]
    elif n > 2:
        fib = [1,1]
        while i < (n-1):
            fib.append(fib[i]+fib[i-1])
            i=i+1
    return fib
print(fibbonaci(n))
