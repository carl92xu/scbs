file = open("studentData.txt", "w")

idInput = input("Student ID: ")
while idInput != "0":
    emailInput = input("Email: ")
    nameEmailInput = idInput+"#"+emailInput
    print(nameEmailInput)
    file.write(nameEmailInput+"\n")
    idInput = input("Student ID: ")
file.close()
print("Exit")
