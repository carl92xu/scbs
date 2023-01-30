searchID = input("Search Student ID: ")
while searchID != str(0):
    file = open("studentData.txt", "r")
    idFound = False
    for line in file.readlines():
        itemSplit = line.split("#")
        if itemSplit[0] == searchID:
            print("Student ID:", itemSplit[0])
            print("Email:", itemSplit[1], end="")
            idFound = True
        else:
            for letter in itemSplit[0]:
                # search for substring
                pass
    file.close()
    if idFound is False:
        print("Student ID not found")
    searchID = input("\nSearch Student ID: ")
print("Exit")
