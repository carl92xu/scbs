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
            self.state = "BIG FISH"


class Fish(Animal):
    def __init__(self, state):
        super().__init__(state, 1)
        self.max_size = 2

    def set_max_size(self, maxsize):
        self.max_size = maxsize

    def feed(self):
        self.size += 2
        print("Fish is now size of", self.size)
        if self.size == self.max_size:
            self.state = "BIG FISH"


class Duck(Animal):
    def __init__(self, state):
        super().__init__(state, 3)

    def feed(self):
        super().feed()
        if self.size == 5:
            self.state = "BIG DUCK"


thisFish = Fish("little fish")
thisFish.set_max_size(3)

thisDuck = Duck("little duck")

for i in range(3):
    thisFish.feed()
    print(thisFish.state)
    thisDuck.feed()
    print(thisDuck.state)
