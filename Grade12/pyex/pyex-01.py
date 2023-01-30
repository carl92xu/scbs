import random


def guess():
    num_int = False
    while not num_int:
        try:
            num = int(input("\nPlease enter your guess: "))
            num_int = True
            while num < 1 or num > 100:
                num = int(input("Please enter a number between 1-100: "))
            return num
        except:
            print("Please enter a whole number!")


print("\033[4mWelcome to the number guessing game.\033[0m\n")
print("The objective is to guess the number I'm thinking of.")
print("I will give you clues after your first guess.")
print("I have thought of a number from 1-100.")
secretNumber = int(random.randint(1, 100))
guessed = False
count = 0
while guessed is False:
    numGuessed = int(guess())
    count += 1
    if numGuessed < secretNumber:
        print("Guess is too low, guess higher!")
    elif numGuessed > secretNumber:
        print("Guess is too high, guess lower!")
    else:
        print("You guessed it!")
        guessed = True
        print("It took you", count, "times.")
