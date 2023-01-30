file = open("studentData2.txt", "a")
idInput = input("Student ID: ")
while idInput != "0":
    emailInput = input("Email: ")
    homeInput = input("Home Address: ")
    tutorInput = input("Tutor: ")
    file.write(idInput+"\n"+emailInput+"\n"+homeInput+"\n"+tutorInput+"\n")
    idInput = input("\nStudent ID: ")
file.close()

searchID = input("\nSearch Student ID: ")
while searchID != str(0):
    file = open("studentData2.txt", "r")
    idFound = False
    printLineFlag = False
    printCount = 0
    for line in file.readlines():
        if line == searchID+"\n":
            idFound = True
            printLineFlag = True
        else:
            # substring search
            pass

        if printLineFlag is True:
            printCount += 1
            if printCount == 1:
                print("Student ID:", line[:-1])
            elif printCount == 2:
                print("Email:", line[:-1])
            elif printCount == 3:
                print("Home Address:", line[:-1])
            elif printCount == 4:
                print("Tutor:", line[:-1])
            elif printCount == 5:
                printLineFlag = False
                break

    file.close()
    if idFound is False:
        print("Student ID not found")
    searchID = input("\nSearch Student ID: ")
print("Exit")
