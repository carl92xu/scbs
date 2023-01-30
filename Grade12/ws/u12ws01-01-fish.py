def feed(state, size):
    size += 1
    print("Fish fed")
    if size == 5:
        state = "FISH"
    return state, size


thisFishState = "Fish"
thisFishSize = 1
print(thisFishState, "is of size", thisFishSize)
while thisFishState != "FISH":
    thisFishState, thisFishSize = feed(thisFishState, thisFishSize)
print("It is now a big", thisFishState)
