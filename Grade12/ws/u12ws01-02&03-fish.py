class Animal:
    def __init__(self, state, size):
        self.state = state
        self.size = size

    def get_state(self):
        return self.state

    def get_size(self):
        return self.size

    def feed(self):
        self.size += 1
        print("Fish is now size of", self.size)
        if self.size == 5:
            self.state = "FISH"


thisFish = Animal("Fish", 1)

print("State:", thisFish.get_state(), "\nSize:", thisFish.get_size())

while thisFish.get_state() != "FISH":
    thisFish.feed()

print("It is now a big", thisFish.get_state())
