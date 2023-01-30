# quiz
import random

# the dictionary that contains the questions (which are the key) and the answers (value)
my_dict = {}

for i in range(50):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    key = str(num1)+"*"+str(num2)
    value = int(num1) * int(num2)
    my_dict[key] = value

'''my_dict = {
    "8 bits make a:": "byte",
    "1024 bytes make a:": "kilobyte",
    "Picture Element...": "A3...",
    "Q4...": "A4..."
}'''
print(my_dict)

print("\nThis quiz has", len(my_dict), "questions")

print("\nQuiz")
print("-------------------------")

playing = True
num = 0
while playing is True:
    score = 0

    while num <= 1 or num > len(my_dict):
        num = int(input("\nHow many questions would you like: "))

    for i in range(num):
        question = (random.choice(list(my_dict.keys())))
        answer = my_dict[question]

        print("\nQuestion", i+1)
        print(question + "?")

        guess = input("Your answer: ")

        if guess.lower() == answer.lower():
            print("Correct")
            score += 1
            del my_dict[question]
        else:
            print("Nope")

    print("\nYour final score was " + str(score))

    again = input("Enter any key to play again, or 'q' to quit: ")

    if again.lower() == "q":
        playing = False
