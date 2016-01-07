

class QuickUnion:
    def __init__(self, size):
        self._array = list(range(size))
        self._size_array = [0] * size

    def __len__(self):
        return len(self.array)

    def find(self, first_index, second_index):
        return self.root(first_index) == self.root(second_index)

    def reduce(self):
        self.array = [root(entry) for entry in self.array]

    def root(self, index):
        while index != self.array[index]:
            self.array[index] = self.array[self.array[index]]
            index = self.array[index]
        return index

    def unite(self, first_index, second_index):
        first_id = self.root(first_index)
        second_id = self.root(second_index)
        if self.size_array[first_id] < self.size_array[second_id]:
            self.array[first_id] = second_id
            self.size_array[second_id] += self.size_array[first_id]
        else:
            self.array[second_id] = first_id
            self.size_array[first_id] += self.size_array[second_id]

    @property
    def array(self):
        return self._array

    @property
    def size_array(self):
        return self._size_array

