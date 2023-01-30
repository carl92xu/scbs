Age = []
SchoolHouse = []
ReactionTime = []

for i in range(2):
    age = int(input("Please enter the age of this student: "))
    while not(age > 11 and age < 17):
        age = int(input("Pleas check the age and enter again: "))
    Age.append(age)

    schoolH = input("Please enter the school house of this student: ")
    while schoolH != "M" and schoolH != "S":
        schoolH = input("Pleas check the house name and enter again: ")
    SchoolHouse.append(schoolH)

    reactionT = int(input("Please enter the reaction time of this student: "))
    while
    ReactionTime.append(reactionT)

print(Age)
print(SchoolHouse)
print(ReactionTime)