import random
coc=random.choice(['rock','scissor','paper'])
print(coc)
plc=input("Your choice:")

while True:
    if coc == 'rock':
        if plc=='r'or'rock':
          print('You got the same.')
        elif plc=='s'or'scissor':
            print('You lose!')
        elif plc =='p'or'paper':
            print('You win!')
        else:
            print("It's not a choice in the game.")

    if coc == 'scissor':
        if plc=='s'or'scissor':
            print('You got the same.')
        elif plc=='p'or'paper':
            print('You lose!')
        elif plc =='r'or'rock':
            print('You win!')
        else:
            print("It's not a choice in the game.")

    if coc == 'paper':
        if plc=='p'or'paper':
            print('You got the same.')
        elif plc=='r'or'rock':
            print('You lose!')
        elif plc =='s'or'scissor':
            print('You win!')
        else:
            print("It's not a choice in the game.")

    i = input('Do you wanna play again?')
    if i == "no":
        break
    elif i=="yes":
        plc=input('Your choice:')
        continue

print('You Quit')