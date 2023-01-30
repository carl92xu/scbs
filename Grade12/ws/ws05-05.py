import random
test1 = []
test2 = []
test3 = []
for i in range(30):
    test1.append(random.randint(50, 100))
    test2.append(random.randint(50, 100))
    test3.append(random.randint(50, 100))


total1 = 0
total2 = 0
total3 = 0
for i in range(len(test1)):
    total1 += test1[i]
    total2 += test2[i]
    total3 += test3[i]

print("total1:", total1)
print("total2:", total2)
print("total3:", total3)
print("total_entire:", total1+total2+total3, "\n")

print("ave1:", total1/30)
print("ave2:", total2/30)
print("ave3:", total3/30)
