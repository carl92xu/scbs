class NodeClass:
    def __init__(self):
        self.__Data = ''

    def set_data(self, d):
        self.__Data = d

    def get_data(self):
        return self.__Data


class StackClass:
    def __init__(self):
        self.__Stack = [NodeClass() for i in range(51)]
        self.__TopOfStackPointer = -1
        self.__MaxSize = 50

    def push_on_stack(self, d):
        if self.__TopOfStackPointer == self.__MaxSize:
            print("Stack is Full")
        else:
            self.__TopOfStackPointer += 1
            self.__Stack[self.__TopOfStackPointer].set_data(d)

    def pop_from_stack(self):
        if self.__TopOfStackPointer == -1:
            return "Stack is Empty"
        else:
            data = self.__Stack[self.__TopOfStackPointer].get_data()
            self.__TopOfStackPointer -= 1
            return data


ThisStack = StackClass()
print(ThisStack.pop_from_stack())
ThisStack.push_on_stack("A")
ThisStack.push_on_stack("B")
ThisStack.push_on_stack("C")
ThisStack.push_on_stack("D")
ThisStack.push_on_stack("E")
print(ThisStack.pop_from_stack())
print(ThisStack.pop_from_stack())
print(ThisStack.pop_from_stack())
