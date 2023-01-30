import random


def generate_mimi():
    mimi = random.randint(1, 5)
    return mimi


def input_guess():
    guess = input("Enter your guess: ")
    return guess


def output_message(guess, mimi, count, flag):
    count += 1
    if int(guess) == int(mimi):
        print("Congratulations, you have guessed", count, "times")
        flag = True
    else:
        print("Bad Luck")
    return flag, count
