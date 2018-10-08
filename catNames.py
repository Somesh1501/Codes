catNames = []
while True :
    print("Eneter the name of your cat " + str(len(catNames) + 1) + "(OR press enter for nothing)")
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print("The Cat names are :")
#for name in catNames:
for name in range(len(catNames)):
    print(str(name ) + " : " + catNames[name])# list concatenation
