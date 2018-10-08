def greater(a,b):
    if (a>b):
        return a
    else:
        return b
def greatest(a,b,c):
    return greater(greater(a,b),c)
    
print('hello')
x=(input("enter 1st number"))
y=(input("enter 2nd number"))
z=(input("enter 3rd number"))
print(greatest(x,y,z))
            

        
