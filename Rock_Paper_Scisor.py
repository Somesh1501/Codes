print("\t\t\t\t\tThis is Rock-Paper-Scissor 2P game.")
user1 = input('Enter your name.(Player 1)\n')
user2 = input('Enter your name.(Player 2)\n')
x = input('%s, What do you want to choose(rock, paper or scissor)'%user1)
y = input('%s, What do you want to choose(rock, paper or scissor)'%user2)
def compare(x,y):
    if x == y:
        print("It's a Tie.")
    elif x == "rock":
        if y == "scissor":
            print('Rock wins.')
        else:
            print("Paper wins.")
    elif x == "paper":
        if y == "rock":
            print('Paper wins.')
        else:
            print('Scissor wins.')
    elif x == "scissor":
        if y == "paper":
            print('Scissor wins.')
        else:
            print('Rock wins.')
    else:
        print('You have entered wrong options.(Please select rock, paper or scissor)')
compare(x,y)