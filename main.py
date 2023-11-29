class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.isempty():
            return self.items.pop(0)
        else:
            raise QueueError("Queue is empty")


class SuperQueue(Queue):
    def isempty(self):
        return super().isempty()

# Приклад використання:
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
