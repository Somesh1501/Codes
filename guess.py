#This program is a no. guessing game
import random
secretNumber = random.randint(1,20)
print('I am thinking a number between 1 to 20')
# This will ask user to take a guess for 6 times
for guessesTaken in range(1,7):
    print('Guess It.....')
    guess = int(input()) # Guessed no. is stored in this variable
    if guess < secretNumber :
        print('Oops! , Your guess is too low try again..')
    elif guess > secretNumber :
        print('Oops! , Your guess is too high try again.. ')
    else :
        break

if guess == secretNumber :
    print("You're Winner , You guessed correct number in " + str(guessesTaken) + ' guesses')
else:
    print("You won't win please refresh the program. ")