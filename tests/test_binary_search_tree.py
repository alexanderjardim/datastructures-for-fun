
import unittest
from d.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_into_empty_tree(self):
        self.bst.insert(10)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.data, 10)
        self.assertEqual(self.bst.root.count, 1)

    def test_insert_smaller_than_root(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.assertIsNotNone(self.bst.root.left)
        self.assertEqual(self.bst.root.left.data, 5)
        self.assertEqual(self.bst.root.left.count, 1)

    def test_insert_larger_than_root(self):
        self.bst.insert(10)
        self.bst.insert(15)
        self.assertIsNotNone(self.bst.root.right)
        self.assertEqual(self.bst.root.right.data, 15)
        self.assertEqual(self.bst.root.right.count, 1)

    def test_insert_multiple_nodes(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(12)
        self.bst.insert(18)

        self.assertEqual(self.bst.root.data, 10)
        self.assertEqual(self.bst.root.left.data, 5)
        self.assertEqual(self.bst.root.right.data, 15)
        self.assertEqual(self.bst.root.left.left.data, 3)
        self.assertEqual(self.bst.root.left.right.data, 7)
        self.assertEqual(self.bst.root.right.left.data, 12)
        self.assertEqual(self.bst.root.right.right.data, 18)

    def test_insert_duplicate_value(self):
        self.bst.insert(10)
        self.bst.insert(10)
        self.assertEqual(self.bst.root.count, 2)
        self.assertIsNone(self.bst.root.right)
        self.assertIsNone(self.bst.root.left)

    def test_insert_multiple_duplicates(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(10)
        self.assertEqual(self.bst.root.count, 3)
        self.assertEqual(self.bst.root.left.count, 2)

    def test_height_of_empty_tree(self):
        self.assertEqual(self.bst.height(), 0)

    def test_height_of_single_node_tree(self):
        self.bst.insert(10)
        self.assertEqual(self.bst.height(), 1)

    def test_height_of_skewed_tree(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(3)
        self.assertEqual(self.bst.height(), 3)

    def test_height_of_balanced_tree(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.height(), 2)
        self.bst.print_tree()

    def test_large_balanced_insertion_tree(self):
        value_range = list(range(1000))
        insertions = 0
        while insertions < 900 and len(value_range) >= 10:
            avg = (value_range[0] + value_range[-1]) // 2
            self.bst.insert(avg)
            self.bst.insert(value_range[0])
            self.bst.insert(value_range[-1])
            insertions += 3
            value_range.pop(0)
            value_range.pop(-1)
        self.assertEqual(self.bst.height(), 301)

if __name__ == '__main__':
    unittest.main()
