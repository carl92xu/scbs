nameList = [2, 4, 1, 0, 5, 7, 3]

for thisPointer in range(1, len(nameList)):
    temp = nameList[thisPointer]
    pointer = thisPointer - 1
    while (nameList[pointer] > temp) and pointer >= 0:
        nameList[pointer+1] = nameList[pointer]
        pointer -= 1
    nameList[pointer+1] = temp

print(nameList)
