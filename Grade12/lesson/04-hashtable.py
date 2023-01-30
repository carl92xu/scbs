def initialise():
    hashTbl = []
    tblSize = int(input("Enter how big you want the table to be: "))
    prime_check = prime_number_check(tblSize)
    while prime_check is False:
        tblSize = int(input("Please enter a prime number: "))
        prime_check = prime_number_check(tblSize)
    for i in range(tblSize):
        hashTbl.append(' ')
    return hashTbl, tblSize


def prime_number_check(num):
    # Ref: https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/  # ALTERED
    flag = False
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num // 2):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                break
        else:
            flag = True

    return flag


def createAddress(item, tblsize):
    return item % tblsize


def ask_if_continue():
    answer = input("Would you like to add another value Y/N: ").upper()
    if answer == "N":
        flag = False
    else:
        flag = True
    return flag


def addItem(hashTbl, tblSize):
    addItem = True
    while addItem is True:
        value = int(input("Enter a number into hash table: "))
        index = createAddress(value, tblSize)
        if hashTbl[index] == "" or hashTbl[index == "/"]:  # improved
            hashTbl[index] = value
        else:
            spaceFound = False
            while spaceFound is False:
                index = (index+1) % tblSize  # improved
                if hashTbl[index] == "":
                    hashTbl[index] = value
                    spaceFound = True
        print(hashTbl)
        addItem = ask_if_continue()
    return hashTbl


def removeItem(hashTbl, tblSize):
    removeItem = True
    while removeItem is True:
        value = int(input("Enter a number into hash table: "))
        index = createAddress(value, tblSize)
        if hashTbl[index] == "":
            print("Number not found")
        elif hashTbl[index == "/"]:
            valueFound = False
            while valueFound is False:
                index = (index + 1) % tblSize
                if hashTbl[index] == "":
                    print("Number not found")
                elif hashTbl[index] == value:
                    # found the item
                    hashTbl[index] = "/"
                    valueFound = True
        else:
            # found the item
            hashTbl[index] = "/"
        print(hashTbl)
        removeItem = ask_if_continue()
    return hashTbl


def searchTbl(value, hashTbl, tblSize):
    searchItem = True
    while searchItem is True:
        index = createAddress(value, tblSize)
        if hashTbl[index] == "":
            print("Number not found")
        elif hashTbl[index == "/"]:
            valueFound = False
            while valueFound is False:
                index = (index + 1) % tblSize
                if hashTbl[index] == "":
                    print("Number not found")
                elif hashTbl[index] == value:
                    # found the item
                    print("Index:", index)
                    valueFound = True
        else:
            # found the item
            print("Index:", index)
        print(hashTbl)
        searchItem = ask_if_continue()
    return hashTbl


# main
table, maxSize = initialise()
while True:
    option = input("Please choose one of the following options:\n1. add new item\n2. remove item\n"
                   "3, search of item\n4. Exit\nYour option: ")

    if option == "1":
        table = addItem(table, maxSize)
    elif option == "2":
        table = removeItem(table, maxSize)
    elif option == "3":
        item = int(input("Enter the item you want to search for"))
        table = searchTbl(item, table, maxSize)
    else:
        break

print("Exit")
