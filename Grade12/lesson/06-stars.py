size_flag = False
while size_flag is False:
    try:
        size = int(input("Size: "))
        size_flag = True
    except:
        size = int(input("Size: "))

print()

for i in range(size):
    if i == 0 or i == (size-1):
        print("*"*size)
    else:
        print("*" + " "*(size-2) + "*")

print()

for i in range(size):
    if i == 0:
        print("*")
    elif i == (size-1):
        print("*"*(size+1))
    else:
        print("*" + " "*i + "*")
