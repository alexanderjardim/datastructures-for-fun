import unittest
from d.stack import Stack

class TestStack(unittest.TestCase):

    def test_push(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.top.data, 1)
        s.push(2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.top.data, 2)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.size, 0)

    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_minimum(self):
        s = Stack()
        s.push(2)
        self.assertEqual(s.minimum, 2)
        s.push(1)
        self.assertEqual(s.minimum, 1)
        s.push(3)
        self.assertEqual(s.minimum, 1)

    def test_maximum(self):
        s = Stack()
        s.push(2)
        self.assertEqual(s.maximum, 2)
        s.push(1)
        self.assertEqual(s.maximum, 2)
        s.push(3)
        self.assertEqual(s.maximum, 3)

    def test_minimum_after_pop(self):
        s = Stack()
        s.push(2)
        s.push(1)
        s.push(3)
        s.pop()
        self.assertEqual(s.minimum, 1)
        s.pop()
        self.assertEqual(s.minimum, 2)

    def test_maximum_after_pop(self):
        s = Stack()
        s.push(2)
        s.push(1)
        s.push(3)
        s.pop()
        self.assertEqual(s.maximum, 2)
        s.pop()
        self.assertEqual(s.maximum, 2)

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size, 0)
        s.push(1)
        self.assertEqual(s.size, 1)
        s.push(2)
        self.assertEqual(s.size, 2)
        s.pop()
        self.assertEqual(s.size, 1)
        s.pop()
        self.assertEqual(s.size, 0)

if __name__ == '__main__':
    unittest.main()