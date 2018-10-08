#program for adding no. given by user
print('hello, This is no. adding program')
x=(input('enter no.'))
y=len(x)
i=0
result=0
while(i<y):
    result = result + int(x[i])
    i = i + 1
print(result)
