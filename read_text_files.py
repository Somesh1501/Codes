#open function
file = open(r"C:\Users\KALYANKAR\Documents\python.txt", 'r')
'''content = file.read()#reads files
print(content)
file.close()#close files
'''
#readlines = reads lines
content = file.readlines()
for line in content[:5]:
    print(line)
file.close()
