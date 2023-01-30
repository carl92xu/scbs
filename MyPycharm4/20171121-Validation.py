while True:

    try:
        var = input("Please enter your ID:")
        break
    except ValueError:
        print("Error, Not Numbers")
    if len(var) == 6:
        break
    elif len(var) != 6:
        print("Incorrect Length")
        continue
print("OK")