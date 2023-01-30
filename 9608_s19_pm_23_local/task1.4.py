# DECLARE nameAndEmail: ARRAY OF STRING
nameAndEmail = []
nameInput = input("Name: ")
while nameInput != "0":
    emailInput = input("Email: ")
    nameEmailInput = nameInput+"#"+emailInput
    print(nameEmailInput)
    nameAndEmail.append(nameEmailInput)
    nameInput = input("Name: ")

# test
# nameAndEmail = ["carl xu#carl@gmail.com", "john zhang#john@gmail.com"]

searchName = input("Search Name: ")
while searchName != 0:
    nameFound = False
    for i in range(len(nameAndEmail)):
        itemSplit = nameAndEmail[i].split("#")
        if itemSplit[0] == searchName:
            print("Email:", itemSplit[1])
            nameFound = True
        else:
            nameSplit = itemSplit[0].split(" ")
            if nameSplit[0] == searchName or nameSplit[1] == searchName:
                print("Name:", itemSplit[0])
                print("Email:", itemSplit[1])
                nameFound = True
    if nameFound is False:
        print("Name not found")
    searchName = input("\nSearch Name: ")

print("Exit")
