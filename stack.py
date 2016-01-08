

class Stack:

    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self.stack)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("pop from empty stack")

    def push(self, item):
        self.stack.append(item)

    @property
    def stack(self):
        return self._stack

