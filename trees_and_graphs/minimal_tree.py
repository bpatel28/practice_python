"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.
"""
from collections import deque


class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


def create_minimal_bst(sorted_array):
    return _create_minimal_bst(sorted_array, 0, len(sorted_array) - 1)


def _create_minimal_bst(sorted_array, start, end):
    if end < start:
        return None
    mid = int((start + end) / 2)
    left_child = _create_minimal_bst(sorted_array, start, mid - 1)
    right_child = _create_minimal_bst(sorted_array, mid + 1, end)
    root = Node(sorted_array[mid], left_child, right_child)
    return root


def __main__():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    bst_root = create_minimal_bst(arr)

    queue = deque()

    queue.append(bst_root)

    lever_order_items = []
    while len(queue) != 0:
        node = queue.popleft()
        lever_order_items.append(node.data)
        if node.left_child:
            queue.append(node.left_child)
        if node.right_child:
            queue.append(node.right_child)

    print(lever_order_items)


__main__()

