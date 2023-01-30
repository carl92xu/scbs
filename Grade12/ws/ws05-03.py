def len_check():
    a = input("Enter part number: ")
    while len(a) != 4:
        a = input("Part number length is 4, please re-enter: ")
    return a


tot_count = 0
old_count = 0
partNum = len_check()

while int(partNum) != 9999:
    tot_count += 1
    partNumEnd = int(partNum[-1])
    if int(partNumEnd) >= 7:
        old_count += 1

    partNum = len_check()

print(tot_count)
print(old_count)
