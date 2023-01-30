def get_initial(name):
    print("Your name starts with:", name[0])


myName = "Carl"
# myName = input("Enter your name: ")
get_initial(myName)


# not working
def get_initial(name, ini):
    ini = name[0]


myName = "Carl"
# myName = input("Enter your name: ")
myIni = str(0)
get_initial(myName, myIni)
print("Your name starts with:", myIni)
