import random
myList = []

for i in range(100):
    myList.append([])
    for j in range(5):
        myList[i].append(random.randint(0, 30))
    print(myList[i])

print("\nTable is:", myList)
print("Row 18 is:", myList[17])
print("Row 18, Column 2 is:", myList[17][1])