import unittest
from d.linked_lists import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

    def test_append(self):
        self.ll.append(4)
        self.assertEqual(self.ll.to_list(), [1, 2, 3, 4])

    def test_append_after(self):
        self.ll.append_after(4, 1)
        self.assertEqual(self.ll.to_list(), [1, 2, 4, 3])

    def test_append_before(self):
        self.ll.append_before(4, 1)
        self.assertEqual(self.ll.to_list(), [1, 4, 2, 3])
        self.ll.append_before(5, 0)
        self.assertEqual(self.ll.to_list(), [5, 1, 4, 2, 3])

if __name__ == '__main__':
    unittest.main()