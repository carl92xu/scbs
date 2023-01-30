# DECLARE nameAndEmail: ARRAY OF STRING
'''nameAndEmail = []
nameInput = input("Name: ")
while nameInput != "0":
    emailInput = input("Email: ")
    nameEmailInput = nameInput+"#"+emailInput
    print(nameEmailInput)
    nameAndEmail.append(nameEmailInput)
    nameInput = input("Name: ")'''

# test
nameAndEmail = ["carl xu#carl@gmail.com", "john zhang#john@gmail.com"]
print(nameAndEmail)

searchName = input("Name to be Deleted: ")
while searchName != str(0):
    nameFound = False
    for i in range(len(nameAndEmail)):
        itemSplit = nameAndEmail[i].split("#")
        if itemSplit[0] == searchName:
            nameAndEmail[i] = "n/a"
            nameFound = True
    if nameFound is False:
        print("Name not found")
    print(nameAndEmail)
    searchName = input("Name to be Deleted: ")

for item in nameAndEmail:
    if item != "n/a":
        itemSplit = item.split("#")
        print("\nName:", itemSplit[0])
        print("Email:", itemSplit[1])
