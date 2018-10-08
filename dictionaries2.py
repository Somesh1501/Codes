# add any element in dictionary

d1 = {'name' : 'somesh' , 'age' : '17 years' }
''''
d1['education'] = '12th std.' # adding element
del d1['education'] #removing element
print(d1)

# key method gives us list of keys
print(d1.keys())
 #value method gives us list of elements
print(d1.values())

# looping in dictionaries
for i in d1.keys(): # for listing keys
    print(i)
for i in d1.values():# for getting values
    print(i)
'''
# items method gives us keys and element
#looping using items
for i,j in d1.items():
    print('key is ' + str(i) + ' & its value is ' + str(j) )
    print('')

