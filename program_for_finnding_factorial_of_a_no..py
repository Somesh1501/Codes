#prgram for finding factorial of no.
def factorial(x):
    a=1
    while (x>=1):
        a= a * x
        x= x - 1
    return a
x=int(input("enter a no. to calculate factorial "))
y=(factorial(x))
print(("factorial of ") + str(x) + ("is ") + str(y))
