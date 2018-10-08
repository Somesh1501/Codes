name = input("Plz, Enter your Name")
def plus():
    print('+',end='')
def dash():
    print('-',end='')
def line():
    for i in range(len(name) + 2):
        plus()
        dash()
def wall():
    print('|',end='')
def name_con():
    for j in range(len(name)):
        print(name[j],end='')
        break
def line():
    for k in range(len(name)+6):
        dash()
        name_con()
line()
