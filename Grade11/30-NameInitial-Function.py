def get_initial(name):
    output = name[0]
    return output


myName = input("Enter your name: ")
print("Your name starts with:", get_initial(myName))
