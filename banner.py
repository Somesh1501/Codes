#! python3
x = str(input('Please, Enter Your Name . \n'))
def star():
    print('*', end='')
def space():
    print(' ')
def line_of_stars():
    for i in range(len(x)+ 8):
        star()
def wall():
    print(".:: ", end='')
def mall():
    print(' ::.', end='')
def TJ():
    print('**********')
    wall()
    print('SK', end= '')
    mall()
    print('')
    print('**********' , end= '')

def banner():
    line_of_stars()
    print('')
    wall()
    print(x , end= '' )
    mall()
    print('')
    line_of_stars()
banner()