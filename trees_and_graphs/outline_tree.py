#     1
#   2   3
# 4  5 6 7
#
#     1
#   1   1
# 0  1 1 0
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f'{self.value}'
    
    def __repr__(self):
        return f'{self.value}'
    
def dfs(root, items):
    if not root:
        return
    items.append(root)
    dfs(root.left, items)
    dfs(root.right, items)

def prune_tree(root):
    if not root:
        return True
    left_result = prune_tree(root.left)
    right_result = prune_tree(root.right)
    if not left_result:
        root.left = None
    if not right_result:
        root.right = None
    if root.value != 1:
        return False
    return True

def bfs(root, items):
    if not root:
        return
    queue = deque()
    queue.append([root])
    while len(queue) != 0:
        current_level = queue.popleft()
        items.append(current_level)
        level = []
        for current in current_level:
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
        if len(level) != 0:
            queue.append(level)

def outline_left(root, items):
    if not root:
        return
    queue = deque()
    queue.append([root])
    while len(queue) != 0:
        current_level = queue.popleft()
        items.append(current_level[0])
        level = []
        for current in current_level:
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
        if len(level) != 0:
            queue.append(level)

def outline_right(root, items):
    if not root:
        return
    queue = deque()
    queue.append([root])
    while len(queue) != 0:
        current_level = queue.popleft()
        items.append(current_level[len(current_level)-1])
        level = []
        for current in current_level:
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
        if len(level) != 0:
            queue.append(level)

def outline_tree(root, items):
    if not root:
        return
    queue = deque()
    queue.append([root])
    while len(queue) != 0:
        current_level = queue.popleft()
        if len(current_level) > 1:
            items.append(current_level[0])
            items.append(current_level[len(current_level)-1])
        elif len(current_level) > 0:
            items.append(current_level[0])
        level = []
        for current in current_level:
            if current.left:
                level.append(current.left)
            if current.right:
                level.append(current.right)
        if len(level) != 0:
            queue.append(level)


root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

tree_items = []
outline_tree(root, tree_items)
print(tree_items)

tree_items = []
root = Node(1, Node(1, Node(0), Node(1)), Node(1, Node(1), Node(0)))
bfs(root, tree_items)
print(tree_items)

prune_tree(root)
tree_items = []
bfs(root, tree_items)
print(tree_items)
