from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)

queue.popleft()  # The first to arrive now leaves
print(queue)
