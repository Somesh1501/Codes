# smallest no. finder program

def smaller(a,b):
    if (a<b):
        return a
    else:
        return b

def smallest(a,b,c):
    return smaller (smaller(a,b),c)

a=input('enter a no.')
b=input('enter a no.')
c=input('enter a no.')
print(smallest(a,b,c))
