def ap(a,l,d):
    result = 0
    for i in range(a,l+1,d):
        print(i)
        result = result + i
    return result

a = int(input('enter first term'))
d = int(input('enter common difference'))
n = int(input('enter no. of terms'))
l= a + (n-1)*d

print('your AP is '+str(ap(a,l,d)))
