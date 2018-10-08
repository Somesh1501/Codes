'''passwordFile = open("E:\pass.txt")
secretPassword = passwordFile.read()
Typedpassword = input('Enter Password  ')
if Typedpassword == secretPassword :
    print('Access granted.')
if Typedpassword == '123456':
    print('It is password that can be put only by an Idiot. ')
else :
    print('Access Denied')
'''
passwordFile = open("E:\pass.txt")
secretPassword = passwordFile.read()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
if typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')