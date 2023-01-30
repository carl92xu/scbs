BiggestSoFar = float(input("BSF: "))
NextNumber = float(input("NN: "))
while NextNumber != 0:
    if NextNumber > BiggestSoFar:
        BiggestSoFar = NextNumber
    NextNumber = float(input("NN: "))
print(BiggestSoFar)