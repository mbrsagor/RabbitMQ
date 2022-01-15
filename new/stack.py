class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def show(self):
        for i in self.items:
            print(i)

    def size(self):
        count = len(self.items)
        print(f"Total size: {count}")

    def empty(self):
        return True if self.size() == 0 else False

    def peek(self):
        return self.items[-1]


stack = Stack()

stack.size()
stack.push(10)
stack.push(20)
stack.push(30)
stack.show()
stack.size()
stack.empty()

print(stack.pop())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.show()
stack.size()
