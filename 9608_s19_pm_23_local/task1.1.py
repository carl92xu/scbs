# DECLARE nameAndEmail: ARRAY OF STRING
nameAndEmail = []
# myStr = "Eric Smythe#eric@email.com"
# nameAndEmail.append(myStr)

nameInput = input("Name: ")
while nameInput != "0":
    emailInput = input("Email: ")
    nameEmailInput = nameInput+"#"+emailInput
    print(nameEmailInput)
    nameAndEmail.append(nameEmailInput)
    nameInput = input("Name: ")

for item in nameAndEmail:
    itemSplit = item.split("#")
    print("Name:", itemSplit[0])
    print("Email:", itemSplit[1])
