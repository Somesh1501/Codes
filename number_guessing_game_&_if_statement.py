# ==(equal to ), =(assignment), !=(not equal to)
print("hello")
print('this is a no. guessing game b/w 1 to 10')
x=input('enter a no.')
x=int(x)
if(x==5):
    print('your guess is right, you win')
else:
    print('oops,your guess is wrong')
    if(x<5):
        print('too low, you lose')
    else:
         print('too high, you lose')
