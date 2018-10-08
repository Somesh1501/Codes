#write text files

#file = open(r"C:\Users\KALYANKAR\Documents\dk.txt", 'a')
#file.write("/n Hello somesh")
#file.close

x = (input('enter the name which you want to give to your file  '))
file = open(r"C:\Users\KALYANKAR\Documents\x.txt" , 'a')
print('write anything')
y = input()
file.write(y)
file.close()
