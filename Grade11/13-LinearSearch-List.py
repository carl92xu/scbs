MyList = []
for i in range(0,7,1):
    MyList.append(i)
print(MyList)

SearchValue = int(input("SearchValue: "))
MaxIndex = 6
Found = False
Index = 0

while Found == False and Index <= MaxIndex:
    if MyList[Index] == SearchValue:
        Found = True
    Index += 1

if Found == True:
    print("SearchValue is found at index",Index-1)
else:
    print("SearchValue not found")