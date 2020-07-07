"""
Stack Data Structure.
Methods: push,pop,get_stack,is_empty,peek
"""


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


if __name__ == "__main__":
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    print(myStack.get_stack())
    myStack.push("C")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.get_stack())
    print(myStack.is_empty())
    print(myStack.peek())
