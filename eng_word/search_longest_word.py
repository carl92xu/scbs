file = open("words.txt", "r")

longest = ""
longest_list = []

for line in file:
    if len(line) > len(longest):
        longest = line
        longest_list = [line]
    elif len(line) == len(longest):
        longest_list.append(line)

file.close()

print(longest)
print(longest_list)
