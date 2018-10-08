#NESTED IF-ELSE
def greatest(a,b,c):
    if (a>b):
        if (a>c):
            return a
        else:
            return c
    else:
        if (b>c):
            if (b>a):
                 return b
            else:
                 return c

x=(input("enter 1st number"))
y=(input("enter 2nd number"))
z=(input("enter 3rd number"))
print(greatest(x,y,z))
            

        
