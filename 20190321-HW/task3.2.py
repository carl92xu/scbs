import random
randRangeTop = 10
randRangeBottom = 0
randNum = []
generateOrNot = input("y or n: ")
while generateOrNot != "n":
    randGenerate = random.randint(randRangeBottom, randRangeTop)
    found = False
    for item in randNum:
        if item == randGenerate:
            found = True
            break
    while found is True:
        randGenerate = random.randint(randRangeBottom, randRangeTop)
        found = False
        for item in randNum:
            if item == randGenerate:
                found = True
                break
    if found is False:
        print(randGenerate)
        randNum.append(randGenerate)
    if len(randNum) < (randRangeTop-randRangeBottom):
        generateOrNot = input("\ny or n: ")
    else:
        break
print("\nExit")
