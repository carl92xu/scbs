x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = []
for i in range(3):
    result.append([])
    for j in range(3):
        result[i].append(0)

for i in range(len(x)):
    for j in range(len(x[i])):
        result[i][j] = x[i][j] + y[i][j]

for item in result:
    print(item)