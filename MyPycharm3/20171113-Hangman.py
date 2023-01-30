import random
words=['occur','percent','period','policy','principle','procedure','process','required','research','response']
cc=random.choice(words)

while True:
    #print(cc)
    word = []
    for letter in cc:
        word.append(letter)
    random.shuffle(word)
    print (word)

    pc=input("Take a guess what the original word is:\n")
    if pc == cc:
        print("You Win!")
    else:
        print("You Lose! The word is",cc)
    p=input("Do you want to play again? (Enter 'yes' to continue, anything else to quit)")

    if p == 'yes':
        continue
    else:
        break

print("You Quit")