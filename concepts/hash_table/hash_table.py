from concepts.hash_table.data_node import DataNode
_INITIAL_CAPACITY = 100
_GROW_FACTOR = 2


class HashTable:
    def __init__(self, capacity=_INITIAL_CAPACITY):
        self._capacity = capacity
        self._data = [None] * self._capacity
        self._count = 0

    def _is_full(self):
        return self._capacity == self._count

    def _grow_size(self):
        self._capacity = self._capacity * _GROW_FACTOR
        temp = self._data
        self._data = [None] * self._capacity
        self._count = 0
        for item in temp:
            while item is not None:
                self.add(item.key, item.value)
                item = item.next_node

    def add(self, key, value):
        if key is None:
            raise Exception("Key can not be none.")
        if self._is_full():
            self._grow_size()
        hash_value = hash(key)
        index = hash_value % self._capacity
        if self._data[index] is None:
            node = DataNode(key, value)
            self._data[index] = node
            self._count += 1
        else:
            curr = self._data[index]
            while curr.next_node is not None:
                if curr.key == key:
                    break
                curr = curr.next_node
            if curr is not None and curr.key == key:
                curr.value = value
            else:
                new_data_node = DataNode(key, value)
                new_data_node.set_prev_node(curr)
                curr.set_next_node(new_data_node)
                self._count += 1

    def _is_half_or_less_capacity(self):
        return len(self) <= self._capacity / 2

    def _reduce_capacity(self):
        self._capacity = int(self._capacity * (1 / _GROW_FACTOR))
        temp = self._data
        self._data = [None] * self._capacity
        self._count = 0
        for item in temp:
            while item is not None:
                self.add(item.key, item.value)
                item = item.next_node

    def remove(self, key):
        if self._is_half_or_less_capacity:
            self._reduce_capacity()
        hash_value = hash(key)
        index = hash_value % self._capacity
        curr = self._data[index]
        if curr is not None and curr.key == key:
            self._data[index] = None
            self._count -= 1
            return
        while curr is not None:
            if curr.key == key:
                next_node = curr.next_node
                prev_node = curr.prev_node
                if prev_node is not None:
                    prev_node.set_next_node(next_node)
                if next_node is not None:
                    next_node.set_prev_node(prev_node)
                self._count -= 1
                del curr
                break
            curr = curr.next_node

    def __iter__(self):
        self._iter_curr = None
        self._iter_counter = -1
        for item in self._data:
            self._iter_counter += 1
            if item is not None:
                self._iter_curr = item
                return self
        return self

    def __next__(self):
        if self._iter_curr is None and self._iter_counter + 1 == self._capacity:
            raise StopIteration()
        curr_item = self._iter_curr
        self._iter_curr = self._iter_curr.next_node
        if self._iter_curr is None:
            for item in self._data[self._iter_counter + 1:]:
                self._iter_counter += 1
                if item is not None:
                    self._iter_curr = item
                    break
        return curr_item.key, curr_item.value

    def __str__(self):
        return f'[{", ".join(map(lambda item: f"{{{item[0]} : {item[1]}}}", self))}]'

    def __getitem__(self, key):
        hash_value = hash(key)
        index = hash_value % self._capacity
        curr = self._data[index]
        while curr is not None:
            if curr.key == key:
                break
            curr = curr.next_node
        if curr is not None:
            return curr.value

    def __len__(self):
        return self._count

    def __del__(self):
        del self._data
        del self._capacity
        del self._count
