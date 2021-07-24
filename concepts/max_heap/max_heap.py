def _parent_index(index):
    return (index - 1) // 2


def _left_child_index(index):
    return (2 * index) + 1


def _right_child_index(index):
    return (2 * index) + 2


class MaxHeap:
    _MAX_SIZE = 10
    _GROW_FACTOR = 2

    def __init__(self, max_size=_MAX_SIZE):
        self._heap = [0] * max_size
        self.size = 0

    def _capacity(self):
        return len(self._heap)

    def _is_leaf_index(self, index):
        return self.size > index > self.size // 2

    def _grow_heap(self):
        self._heap += [0] * (len(self._heap) * self._GROW_FACTOR)

    def _swap(self, pos1, pos2):
        self._heap[pos1], self._heap[pos2] = self._heap[pos2], self._heap[pos1]

    def insert(self, item):
        if self.size >= self._capacity():
            self._grow_heap()
        self.size += 1
        self._heap[self.size-1] = item
        current = self.size-1
        while _parent_index(current) >= 0 and self._heap[current] > self._heap[_parent_index(current)]:
            self._swap(current, _parent_index(current))
            current = _parent_index(current)

    def _heapify(self, index):
        if not self._is_leaf_index(index):
            left_child_index = _left_child_index(index)
            right_child_index = _right_child_index(index)
            if self._heap[index] < self._heap[left_child_index] or self._heap[index] < self._heap[right_child_index]:
                if self._heap[right_child_index] > self._heap[left_child_index]:
                    self._swap(index, right_child_index)
                    self._heapify(right_child_index)
                else:
                    self._swap(index, left_child_index)
                    self._heapify(left_child_index)

    def remove_max(self):
        if self.size == 0:
            return
        max_value = self._heap[0]
        self._swap(0, self.size-1)
        self._heap[self.size - 1] = 0
        self.size -= 1
        self._heapify(0)
        return max_value
