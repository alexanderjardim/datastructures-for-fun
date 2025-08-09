class Node:
    """A class representing a node in a singly linked list."""
    def __init__(self, data):
        """Initializes a new node with the given data."""
        self.data = data
        self.next = None

class LinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None
        self.size = 0

    def to_list(self):
        """Converts the linked list to a Python list.

        Returns:
            list: A list containing the data of the linked list in order.
        """
        result_list = []
        current_node = self.head
        while current_node:
            result_list.append(current_node.data)
            current_node = current_node.next
        return result_list

    def append(self, data):
        """Appends a new node with the given data to the end of the linked list.

        Args:
            data: The data to be added to the new node.
        """
        if not self.head:
            self.head = Node(data)
            self.size += 1
            return
        current_node = self.head
        while current_node:
            if not current_node.next:
                current_node.next = Node(data)
                self.size += 1
                return
            current_node = current_node.next

    def append_before(self, data, target):
        """Inserts a new node with the given data before the target index.

        Args:
            data: The data to be added to the new node.
            target: The index before which the new node is to be inserted.
        """
        if target == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        previous_node = self.head
        current_node = previous_node.next
        position = 1
        while current_node:
            if target == position:
                new_node = Node(data)
                new_node.next = current_node
                previous_node.next = new_node
                return
            position += 1
            previous_node = current_node
            current_node = current_node.next

    def append_after(self, data, target):
        """Inserts a new node with the given data after the target index.

        Args:
            data: The data to be added to the new node.
            target: The index after which the new node is to be inserted.

        Raises:
            LookupError: If the target index is not found in the linked list.
        """
        current_node = self.head
        position = 0
        while current_node:
            if position == target:
                new_node = Node(data)
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                return
            position += 1
            current_node = current_node.next
        raise LookupError(f"Target {target} not found. The size of the linked list is {position}.")


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll.to_list())