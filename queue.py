

class Queue:

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self.queue)

    def __bool__(self):
        return len(self) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self:
            return self.queue.pop(0)

    @property
    def queue(self):
        return self._queue
