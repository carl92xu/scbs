def pretty_print():
    print("\n{:16s}{:16s}{:16s}{:16s}".format("Student Name:", "Email Address:", "Date of Birth:", "Student ID:"))
    for i in range(len(studentTable)):
        print("{:16s}{:16s}{:16s}{:16s}".format(studentTable[i][0], studentTable[i][1], studentTable[i][2],
                                                studentTable[i][3]))


record = 2
field = 4
studentTable = [["e"]*field for i in range(record)]

pretty_print()
