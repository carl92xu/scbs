file = open("og_processed.txt", "r")
CORRECT_ORDER = ['D', 'L', 'G', 'J', 'A', 'H', 'G', 'K', 'E', 'I', 'G', 'C', 'B', 'G', 'F', 'D']

names = []
name_count = []
name_rec = []

for line in file.readlines():
    time = line[:8]
    point = line[9]
    name = line[11:].strip("\n")
    if name not in names:
        names.append(name)
        name_count.append(1)
        name_rec.append([point])
    else:
        name_index = names.index(name)
        if str(name_rec[name_index][-1]) != str(point):
            name_rec[name_index].append(point)
            name_count[name_index] += 1

file.close()

# print(names)
# print(len(names))
# print(name_count)
# print(len(name_count))

for i in range(len(names)):
    if name_rec[i] != CORRECT_ORDER and names[i] != "jeanne":
        print("{:}    {:}    {:}".format(names[i], name_count[i], name_rec[i]))
