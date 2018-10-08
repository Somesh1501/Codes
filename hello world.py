import random
a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
list1 = range(a,b)
list2 = range(c,d)
list3 = [i for i in list1 and list2 if list1[i] == list2[i]]
print(list3)