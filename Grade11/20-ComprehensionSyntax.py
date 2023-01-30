squares1 = []
for i in range(1, 6):
    squares1.append(i**2)
print("squares1:", squares1)

squares2 = [j**2 for j in range(1, 6)]
print("squares2:", squares2)

list1 = [k for k in range(1, 10) if k % 2 != 0]
squares3 = [item**item for item in list1]
print("squares3:", squares3)

squares4 = [k for k in range(1, 11) if 10 % k == 0]
print("squares4:", squares4)

list2 = [1, 3, 6, 3, 8]
for i in range(len(list2)):
    list2[i] = 0
print("list2:", list2)

list3 = [1, 3, 6, 3, 8]
list3 = [0 for i in range(len(list3))]
print("list3:", list3)