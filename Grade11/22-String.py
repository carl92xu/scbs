str1 = 'Hi'
str2 = 'Nid'
print(str1+" "+str2)

state = "California"
print(len(state))
print(state[-4])

emptyStr = ""
print(len(emptyStr))

for letter in state:
    print(letter, end=letter)

print()
count = 0
while count < len(state):
    print(state[count], end=" ")
    count += 1

subState = state[4:7]
print("\n"+subState)

myName = "John Zhang"
givenName = myName[0:4]
lastName = myName[5:len(myName)]
print(givenName, lastName)