INITIAL_SIZE = 10
SIZE_FACTOR = 1


class ArrayList:
    def __init__(self, *data, length=INITIAL_SIZE):
        if length <= 0:
            length = INITIAL_SIZE
        self._capacity = length if length > len(data) else len(data) * 2
        self._data = [None] * self._capacity
        self._last_element_index = len(data) - 1
        self._iter_index = -1
        for i in range(len(data)):
            self._data[i] = data[i]

    def _is_full(self):
        return self._capacity == len(self)

    def _grow_size(self):
        self._data = self._data + ([None] * len(self) * SIZE_FACTOR)
        self._capacity = len(self._data)

    def append(self, item):
        if self._is_full():
            self._grow_size()
        if self._last_element_index < self._capacity:
            self._last_element_index += 1
        self._data[self._last_element_index] = item

    def _is_more_then_half_empty(self):
        return len(self) * 2 <= self._capacity

    def _reduce_size(self):
        if len(self) * 2 <= self._capacity:
            self._data = self._data[0:len(self) * 2]
        else:
            self._data = self._data[0:len(self)] + ([None] * len(self) * SIZE_FACTOR)
        self._capacity = len(self._data)

    def remove(self, item):
        if self._is_more_then_half_empty():
            self._reduce_size()
        remove_index = -1
        for i in range(0, len(self)):
            if item == self._data[i]:
                remove_index = i
                break
        if remove_index == -1:
            raise Exception("No Item found!")
        self._data = self._data[0:remove_index] + self._data[remove_index+1:]
        self._last_element_index -= 1

    def insert(self, index, item):
        if index > len(self) or index < 0:
            raise IndexError()
        if self._is_full():
            self._grow_size()
        self._data = self._data[0:index] + [item] + self._data[index:]
        self._last_element_index += 1

    def __len__(self):
        return self._last_element_index + 1

    def __iter__(self):
        return self

    def __next__(self):
        self._iter_index += 1
        if self._iter_index > self._last_element_index:
            raise StopIteration()
        return self._data[self._iter_index]

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise TypeError()
        if i < 0:
            i = self._last_element_index + i + 1
        if i > self._last_element_index or i < 0:
            raise IndexError()
        return self._data[i]

    def __contains__(self, item):
        for val in self._data[0:len(self)]:
            if val == item:
                return True
        return False

    def __str__(self):
        return f'[{", ".join(map(lambda num: str(num), self._data[0:len(self)]))}]'
