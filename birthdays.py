birthdays = {'mom' : 'june 24' , 'dad' : 'july 1' , 'Aakash' : 'sept 1'}

while True:
    print("Enter a Name. (Leave Blank to quit.)")
    name = input()
    if name == "" :
        break
    if name in birthdays :
        print(birthdays[name] + " is birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is " + name + "'s birthday")
        bday = input()
        birth = birthdays.setdefault(name , bday)
        print("Birthday database is updated.")