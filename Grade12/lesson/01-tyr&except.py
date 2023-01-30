number_entered = False
while not number_entered:
    try:
        n = int(input("Enter a whole number: "))
        number_entered = True
    except:
        print("Must be a whole number!")
