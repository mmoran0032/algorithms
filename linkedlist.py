

from node import Node


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __bool__(self):
        return self.head != None

    def __len__(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def remove(self, item):
        previous = self.head
        current = self.head
        while current is not None and current.data != item:
            previous = current
            current = current.next
        else:
            if current.data == item:
                previous.next = current.next

    def find(self, item):
        current = self.head
        while current is not None and current.data != item:
            current = current.next
        return current is not None

    def append(self, item):
        # O(n) method without tail
        # previous = self.head
        # tail = self.head
        # while tail is not None:
        #     previous = tail
        #     tail = tail.next
        # else:
        #     if previous is not None:
        #         previous.next = Node(item)
        #     else:
        #         self.head = Node(item)
        # O(1) method with tail
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.add(item)

    def insert(self, item, position):
        new_node = Node(item)
        current_position = 0
        previous = self.head
        current = self.head
        while current_position != position and current is not None:
            previous = current
            current = current.next
            current_position += 1
        else:
            if current is not None:
                new_node.next = current
                if previous is not None:
                    previous.next = new_node
                else:
                    self.head = new_node
