class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self):
        return self.height * self.length

    def perimeter(self):
        return 2 * (self.height + self.length)

    def set_height(self, height):
        self.height = height

    def set_length(self, length):
        self.length = length

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length


r1 = Rectangle(10, 20)
print("r1 area:", r1.area())
