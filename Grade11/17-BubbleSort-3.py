import random
myList = []

for i in range(100):
    myList.append(random.randint(-1000, 1000))
print("Original:", myList)

length = len(myList)
cache = 0

for i in range(len(myList)-1):
    for j in range(length-1):
        if myList[j] > myList[j + 1]:
            cache = myList[j]
            myList[j] = myList[j + 1]
            myList[j + 1] = cache
    length -= 1
print("Sorted:  ", myList)