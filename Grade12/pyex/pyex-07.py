import random
print("Welcome to Hangman!")

file = open("words.txt", "r")
wordList = file.read().split("\n")
file.close()
word = list(wordList[random.randint(0, len(wordList))].lower())
print(word)
# input("Press Enter")

# create guessed_word underlines
guessed_word = ""
for i in range(len(word)):
    guessed_word += "_"
guessed_word = list(guessed_word)
# print(guessed_word)
# input("Press Enter")

guessed_letters = []
lives = 10
wordGuessed = False

while lives >= 1 and not wordGuessed:

    print("\n" + " ".join(guessed_word))

    user_guess = input("Guess a letter/word! (" + str(lives) + " Lives remaining)\n").lower()

    # Check if letter is in the word
    letter_in_word = False
    for i in range(len(word)):
        # if user_guess == word[i] or list(user_guess) == word:
        if user_guess == word[i]:
            # guessed_word[i] = user_guess[i]
            guessed_word[i] = user_guess
            letter_in_word = True

    if letter_in_word is False:
        lives -= 1

        # Store incorrect letter into list
        letter_in_list = False
        for item in guessed_letters:
            if item == user_guess:
                letter_in_list = True
        if letter_in_list is False:
            guessed_letters.append(user_guess)

        # print("Incorrect")
    # else:
        # print("Correct")
    print("Guessed letters:", guessed_letters)

    # if guessed_word == word:
    if guessed_word == word or list(user_guess) == word:
        print("\n" + " ".join(guessed_word))
        print("You have guessed the word correctly!")
        wordGuessed = True
    elif lives < 1:
        print("You failed to guess the word correctly :(")
