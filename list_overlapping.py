import random
a = random.sample(range(1,100), 12)
b = random.sample(range(1,100), 16)
list = [i for i in a if i in b]
print(list)
print(a)
print(b)