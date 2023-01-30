def pretty_print():
    print("\n{:16s}{:16s}{:16s}{:16s}".format("Student Name:", "Email Address:", "Date of Birth:", "Student ID:"))
    for i in range(len(studentTable)):
        print("{:16s}{:16s}{:16s}{:16s}".format(studentTable[i][0], studentTable[i][1], studentTable[i][2],
                                                studentTable[i][3]))


studentTable = []
nameInput = input("Input Name: ")
while nameInput != "0":
    emailInput = input("Input Email: ")
    dobInput = input("Input Date of Birth: ")
    idInput = input("Input Student ID: ")
    appendText = [nameInput, emailInput, dobInput, idInput]
    studentTable.append(appendText)
    print(appendText)
    nameInput = input("\nInput Name: ")

pretty_print()

searchName = input("\nSearch Name: ")
while searchName != 0:
    nameFound = False
    for i in range(len(studentTable)):
        nameInList = studentTable[i][0].split(" ")
        if nameInList == searchName:
            print("Name:", studentTable[i][0])
            print("Email:", studentTable[i][1])
            print("Date of Birth:", studentTable[i][2])
            print("Student ID:", studentTable[i][3])
            nameFound = True
        else:
            nameSplit = studentTable[i][0].split(" ")
            if nameSplit[0] == searchName or nameSplit[1] == searchName:
                print("Name:", studentTable[i][0])
                print("Email:", studentTable[i][1])
                print("Date of Birth:", studentTable[i][2])
                print("Student ID:", studentTable[i][3])
                nameFound = True
    if nameFound is False:
        print("Name not found")
    searchName = input("\nSearch Name: ")
