import random

guessesTaken = 0

print("Hello! What is your name?")
myName = input()
    
number = random.randint(1,100)
print('Okay,'+ myName +' There was a boy whose name is Carl, he is originally 1000000 stupid,\n now I am thinking of a number between 1 and 100 which is the times of his stupidness now.\n Guess this number in between 1 to 100')

while guessesTaken < 8:
    print('Take a Guess.')
    guess = input()
    guess = int(guess)
      
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low, he is much mre stuidier')

    elif guess > number:
        print('Your guess is too high, he is a bit smarter')

    else:
        break

if guess == number:
  
        print('Well done, ',myName,'!You guessed his stupidness in ', guessesTaken ,' guesses! \nHe is now ',1000000*guess,' stupid')

elif guess !=number:
        number = str(number)
        print('Nope. the number of times of his stupidness is' + number)

