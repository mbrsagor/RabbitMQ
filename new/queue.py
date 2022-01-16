class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def show(self):
        for i in self.items:
            print(i, end=' ')

    def size(self):
        return len(self.items)

    def is_empty(self):
        return True if self.size() == 0 else False


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)


queue.show()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.show()
