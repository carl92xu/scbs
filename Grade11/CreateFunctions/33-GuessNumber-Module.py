import GuessNumUtility as gnu


mimi = gnu.generate_mimi()
count = 0
guessed = False
while guessed is False:
    guess = gnu.input_guess()
    guessed, count = gnu.output_message(guess, mimi, count, guessed)
print("Exit")
