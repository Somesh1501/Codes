# great no. finder
# try
# except
print('enter two values')
x = input('enter first number :  ')
y = input('enter second number : ')
while True:
    try :
        if int(x) > int(y) :
            print(x + ' is greater number.')
        else :
            print(y + ' is greater number.')
            
    except :
        print('You did not entered numeric values')
        print('please input again')
        x = input('enter first number :  ')
        y = input('enter second number : ')
        continue
    else :
        print('two no. compared successfully.')
        break
