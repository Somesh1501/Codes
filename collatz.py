# This program is based on collatz conjector
def collatz(n):
    while n != 1 :
        if n % 2 == 0:
            n = n // 2
            print(n)
        elif n % 2 == 1 :
            n = 3 * n + 1
            print(n)
def user ():
    try:
        print("Please Enter a Number.")
        num = int(input())
        collatz(num)
    except ValueError :
        print("Enter a valid number")

user()