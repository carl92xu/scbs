def find_char(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i


UserName = "Zhiyun Zhang"
SpaceIndex = find_char(UserName, " ")
FirstName = UserName[:SpaceIndex]
LastName = UserName[SpaceIndex+1:]
print(LastName, FirstName, "在这里！！！")
