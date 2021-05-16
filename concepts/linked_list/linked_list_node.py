class LinkedListNode:
    def __init__(self, data=None, next_node=None, prev_node=None):
        if next_node is not None and type(next_node) is not LinkedListNode:
            raise TypeError("next_node must be type of LinkedListNode.")
        if prev_node is not None and type(prev_node) is not LinkedListNode:
            raise TypeError("prev_node must be type of LinkedListNode.")
        self._data = data
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def next_node(self):
        return self._next_node

    def set_next_node(self, val):
        self._next_node = val

    @property
    def prev_node(self):
        return self._prev_node

    def set_prev_node(self, val):
        self._prev_node = val

    def __str__(self):
        return f"{self._data}"

    def __repr__(self):
        if self._next_node is not None and self._prev_node is not None:
            return f"data : {self._data}, next -> {self._next_node.data}, prev -> {self._prev_node.data}"
        if self._next_node is not None:
            return f"data : {self._data}, next -> {self._next_node.data}, prev -> None"
        if self._prev_node is not None:
            return f"data : {self._data}, next -> None, prev -> {self._prev_node.data}"
        return f"data : {self._data}, next -> None, prev -> None"

    def __eq__(self, other):
        if type(other) is not LinkedListNode:
            return False
        return self._data == other.data
