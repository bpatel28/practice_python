INITIAL_SIZE = 10
SIZE_FACTOR = 1


class ArrayList:
    def __init__(self, *data, length=INITIAL_SIZE):
        if length <= 0:
            length = INITIAL_SIZE
        self._size = length if length > len(data) else len(data) * 2
        self._data = [None] * self._size
        self._last_element_index = len(data) - 1
        self._iter_index = -1
        for i in range(len(data)):
            self._data[i] = data[i]

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

    def _is_full(self):
        return self._size == len(self)

    def _grow_size(self):
        self._data = self._data + ([None] * len(self) * SIZE_FACTOR)
        self._size = len(self._data)

    def append(self, item):
        if self._is_full():
            self._grow_size()
        if self._last_element_index < self._size:
            self._last_element_index += 1
        self._data[self._last_element_index] = item
