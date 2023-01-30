Name = ['John', 'Carl', 'Jason'] #1D List
Age = [16, 17, 18] #1D List
print(Name)
print(Age)

SearchValue = str(input("SearchValue: ")) #String
MaxIndex = 2 #Integer
Found = False #Boolean
Index = 0 #Integer

while Found == False and Index <= MaxIndex:
    if Name[Index] == SearchValue:
        Found = True
    Index += 1

if Found == True:
    print(Name[Index-1], Age[Index-1])
else:
    print("SearchValue not found")