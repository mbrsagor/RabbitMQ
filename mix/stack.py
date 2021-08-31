class Stack(object):

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


my_stack = Stack()
print(my_stack.push("Python"))
print(my_stack.push("JavaScript"))
print(my_stack.pop())
print(my_stack.size())
