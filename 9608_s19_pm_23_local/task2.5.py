file = open("studentData2.txt", "w")

idInput = input("Student ID: ")
while idInput != "0":
    emailInput = input("Email: ")
    homeInput = input("Home Address: ")
    tutorInput = input("Tutor: ")
    file.write(idInput+"\n"+emailInput+"\n"+homeInput+"\n"+tutorInput+"\n")
    idInput = input("\nStudent ID: ")
file.close()
print("Exit")
