from time import sleep


class Animal:
    def __init__(self, state, age):
        self.state = state
        self.Age = age

    def setState(self, state):
        self.state = state

    def setAge(self, Age):
        self.Age = Age

    def getState(self):
        return self.state

    def getAge(self):
        return self.Age

    def age(self):
        self.Age += 1
        print("Bear is", self.Age, "month old.")
        sleep(0.2)
        if self.Age == 24:
            self.state = "BEAR-Let him go into the wild"

    def changeName(self, newName):
        self.state = newName


animal1 = Animal("little bear", 2)
animal1.setState("Found bear")
animal1.setAge(2)

print(animal1.getState(), "is", animal1.getAge(), "months old")

while animal1.getState() != "BEAR-Let him go into the wild":
    animal1.age()

animal1.changeName("Mega Bear")
print("It is now a", animal1.getState())
