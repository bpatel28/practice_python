class DataNode:
    def __init__(self, key=None, value=None, next_node=None, prev_node=None):
        if next_node is not None and type(next_node) is not LinkedListNode:
            raise TypeError("next_node must be type of LinkedListNode.")
        if prev_node is not None and type(prev_node) is not LinkedListNode:
            raise TypeError("prev_node must be type of LinkedListNode.")
        self._key = key
        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, val):
        self._key = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

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
        return f"{self._key}"

    def __repr__(self):
        if self._next_node is not None and self._prev_node is not None:
            return f"data : {self._key}, next -> {self._next_node.data}, prev -> {self._prev_node.data}"
        if self._next_node is not None:
            return f"data : {self._key}, next -> {self._next_node.data}, prev -> None"
        if self._prev_node is not None:
            return f"data : {self._key}, next -> None, prev -> {self._prev_node.data}"
        return f"data : {self._key}, next -> None, prev -> None"

    def __eq__(self, other):
        if type(other) is not DataNode:
            return False
        return self._key == other.data

    def __del__(self):
        del self._key
        del self._value
