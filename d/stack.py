class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self._minimum = []
        self._maximum = []

    @property
    def maximum(self) -> int:
        return self._maximum[-1]

    @property
    def minimum(self) -> int:
        return self._minimum[-1]



    def push(self, data: int):
        if not self.top:
            self.top = Node(data)
            self._minimum.append(data)
            self._maximum.append(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self._minimum.append(min(data, self._minimum[-1]))
            self._maximum.append(max(data, self._maximum[-1]))
        self.size += 1

    def pop(self) -> int:
        if not self.top:
            raise IndexError("Stack is empty")
        v = self.top.data
        self.top = self.top.next
        self.size -= 1
        self._minimum.pop()
        self._maximum.pop()
        return v