"""
Given a binary tree, design an algorithm which creates a linked list of all nodes at each depth.
(e.g., if you have a tree with depth D, you'll have D linked lists.).
"""
from collections import deque


class Node:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.data)


def list_of_depths(root):
    depth_list = []
    queue = deque()

    if root:
        queue.append(root)

    while len(queue) != 0:
        depth_list.append(queue)
        parents = queue
        queue = deque()
        for parent in parents:
            if parent.left_child:
                queue.append(parent.left_child)
            if parent.right_child:
                queue.append(parent.right_child)
    return depth_list


# def list_of_depths(root):
#     depth_list = []
#     _list_of_depths(root, depth_list, 0)
#     return depth_list
#
#
# def _list_of_depths(root, depth_list, level_no):
#     if not root:
#         return
#
#     if len(depth_list) == level_no:
#         depth_items = deque()
#         depth_list.append(depth_items)
#     else:
#         depth_items = depth_list[level_no]
#
#     depth_items.append(root)
#
#     _list_of_depths(root.left_child, depth_list, level_no + 1)
#     _list_of_depths(root.right_child, depth_list, level_no + 1)


def __main__():
    root = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
    for depth in list_of_depths(root):
        print(", ".join(str(item) for item in depth))


__main__()
