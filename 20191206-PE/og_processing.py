file = open("og.txt", "r")
file2 = open("og_processed.txt", "w")
CORRECT_ORDER = ['D', 'L', 'G', 'J', 'A', 'H', 'G', 'K', 'E', 'I', 'G', 'C', 'B', 'G', 'F', 'D']

names = []
name_count = []
name_rec = []
previous_name = ""

for line in file.readlines():
    write = True
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
        else:
            write = False
    if write:
        file2.writelines("{}	{}	{}\n".format(time, point, name))

file.close()
file2.close()
