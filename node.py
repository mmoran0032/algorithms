

class Node:

    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_item):
        self._next = new_item
