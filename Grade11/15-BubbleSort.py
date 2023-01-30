myList = [25, 34, 98, 7, 41, 19, 5]
length = len(myList)
count = 0
cache = 0
while count < len(myList)-1:
    for i in range(length-1):
        if myList[i] > myList[i+1]:
            cache = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = cache
    length -= 1
    count += 1
print(myList)