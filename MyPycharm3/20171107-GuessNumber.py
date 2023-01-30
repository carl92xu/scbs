import random
num = random.randint(1,100)
tries = 0
#Test
#print(num)

number=[]

while True:
    tries = tries + 1
    while True:
        try:
            i = int(input("Please guess a number between 1 and 100:"))
            if i in number:
                print("You have tried it already.")
            number.append(i)
            #Test
            #print(number)
            break
        except ValueError:
            print("Oops! It's not a number.")
    if tries == 6:
        print('Too many guesses')
        print(num)
        break
    if i == num:
        print('You win!!!')
        break
    elif i > 100:
        print("Oops! It's not between 1 and 100.")
    elif i < 1:
        print("Oops! It's not between 1 and 100.")
        break
    elif i < num:
        print('Try Higher.')
    elif i > num:
        print('Try Lower.')
