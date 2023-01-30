class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# main
myStr = input("Please enter a word or phrase to be tested (within 30 chars): ").lower()
# ...
list1 = list(myStr)
print(list1)
numChar = len(list1)
s = Stack()

for char in list1:
    s.push(char)

list2 = []
for char in range(numChar):
    list2.append(s.pop())
print(list2)

if list1 == list2:
    print(True)
else:
    print(False)
