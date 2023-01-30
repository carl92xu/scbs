print("hi"*7)

lcs = [0]*8
lcs[4] = 4
lcs.insert(5,5)
print(lcs)

temp = [[0]*16 for i in range(5)]
print(temp)
temp[0][-1] = 77
print(temp)