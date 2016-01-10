

class Stack:

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return len(self) == 0

    def pop(self):
        if self:
            return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    @property
    def stack(self):
        return self._stack

