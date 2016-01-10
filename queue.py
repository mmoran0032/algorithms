

class Queue:

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self.queue)

    def __bool__(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self:
            return self.queue.pop(0)

    @property
    def queue(self):
        return self._queue
