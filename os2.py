#os module
#getcwd = get current working directory
import os
#chdir = change directory
os.chdir(r"C:\Users\KALYANKAR\Desktop")

x = (input('enter the name which you want to give to your file  '))
file = open(r"C:\Users\KALYANKAR\Desktop\x.txt" , 'a')
print('write anything')
y = input()
file.write(y)
file.close()
