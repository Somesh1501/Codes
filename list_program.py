#kitne items ki list banani hai
x = int(input('how many items you want to store in a list'))
items = []
i = 0
while(i<x):
    y =str (input('what items should you want to add in your list ?'))
    items.append(y)
    i=i+1
z = sorted(items)
print(('your list in alphabetically order ')+str(z))
print('do you want to change any item in your list  : yes/no ?')
a = str(input())
if(a=='yes'):
    b = input('which item you want to change ? ')
    c = z.index(b)
    print(('okay which item you want at place of ')+ str(b))
    t = str(input())
    z[c] = t
    print('now your complete list is ' + str(z))
if(a=='no'):
    print('thank you')
