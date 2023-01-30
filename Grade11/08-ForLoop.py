NumOfNum = int(input("How many numbers in total: "))
BiggestSoFar = input("Number1: ")
count = int(1)
while count < NumOfNum:
    count += 1
    NextNum = input("Number"+str(count)+": ")
    if NextNum > BiggestSoFar:
        BiggestSoFar = NextNum
print("The biggest one is", BiggestSoFar+".")