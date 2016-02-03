#!/usr/bin/env python3


import unittest

from linkedlist import UnorderedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = UnorderedList()

    def test_empty(self):
        self.assertFalse(self.ll)
        self.assertEqual(0, len(self.ll))

    def test_add_item(self):
        self.ll.add(1)
        self.assertEqual(1, self.ll.head.data)

    def test_items_in_reverse_order_added(self):
        self.add_many()
        self.assertEqual(3, self.ll.head.data)
        self.assertEqual(1, self.ll.tail.data)

    def test_append(self):
        self.add_many()
        self.ll.append(4)
        self.assertEqual(4, self.ll.tail.data)

    def test_append_when_empty(self):
        self.ll.append(7)
        self.assertEqual(7, self.ll.head.data)

    def test_find(self):
        self.add_many()
        self.assertTrue(self.ll.find(3))
        self.assertFalse(self.ll.find(5))

    def test_insert(self):
        self.add_many()
        self.ll.insert(4, 1)
        self.assertEqual(4, self.ll.head.next.data)

    def test_insert_out_of_bounds(self):
        self.add_many()
        self.ll.insert(4, 100)
        self.assertEqual(3, len(self.ll))

    def add_many(self):
        self.ll.add(1)
        self.ll.add(2)
        self.ll.add(3)


if __name__ == '__main__':
    unittest.main()
