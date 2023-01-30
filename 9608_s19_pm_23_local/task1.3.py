# DECLARE nameAndEmail: ARRAY OF STRING
nameAndEmail = []

nameInput = input("Name: ")
while nameInput != "0":
    emailInput = input("Email: ")
    nameEmailInput = nameInput+"#"+emailInput
    print(nameEmailInput)
    nameAndEmail.append(nameEmailInput)
    nameInput = input("Name: ")

searchName = input("Search Name: ")
while searchName != 0:
    nameFound = False
    for i in range(len(nameAndEmail)):
        itemSplit = nameAndEmail[i].split("#")
        if itemSplit[0] == searchName:
            print("Email:", itemSplit[1])
            nameFound = True
    if nameFound is False:
        print("Name not found")
    searchName = input("Search Name: ")

print("Exit")
