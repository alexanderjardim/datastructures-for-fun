class Node:
    """A class representing a node in a Binary Search Tree."""
    def __init__(self, data):
        """Initializes a new node with the given data."""
        self.data = data
        self.left = None
        self.right = None
        self.count = 1   


class BinarySearchTree:
    """A class representing a Binary Search Tree."""
    def __init__(self):
        """Initializes an empty Binary Search Tree."""
        self.root = None
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        c = self.root
        while c:
            if data < c.data:
                if c.left is None:
                    c.left = Node(data)
                    return
                c = c.left
            elif data > c.data:
                if c.right is None:
                    c.right = Node(data)
                    return
                c = c.right
            else:
                c.count += 1
                return
    
    def height(self):
        return  self._height(self.root)
    
    def _height(self, node):
        n = node
        hl = 0
        hr = 0
        if n:
            hl += self._height(n.left)+1
            hr += self._height(n.right)+1
        return max(hl, hr)

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node, prefix="", is_left=True):
        if not node:
            return
        if node.right:
            self._print_tree_recursive(node.right, prefix + ("    " if is_left else "|   "), False)
        print(prefix + ("+-- " if is_left else "+-- ") + str(node.data) + (f'({node.count})' if node.count > 1 else ''))
        if node.left:
            self._print_tree_recursive(node.left, prefix + ("|   " if is_left else "    "), True)




