# function for finding position of second word in a string
def position(a,b):
    d= (a.find(b))
    return(a.find(b,d+1))
x=("i like to play guitar,i learning guitar")
y=(position(x,'guitar'))
print(y)
print(x[y:])
