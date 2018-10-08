#program for print AP series
def ap(a,d,l):
    while(a<=l):
        print(a)
        a = a + d

a = int(input("enter 1st term of an AP "))
d = int(input("enter difference b/w an AP. "))
n = int(input("enter no. of terms of an AP "))
l = a + n*d - d
print(str(ap(a,d,l)))
