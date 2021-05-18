from concepts.linked_list import LinkedList


class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self._data = data
        self._left_child = left_child
        self._right_child = right_child

    @property
    def data(self):
        return self._data

    def set_data(self, val):
        self._data = val

    @property
    def left_child(self):
        return self._left_child

    def set_left_child(self, val):
        if val and not isinstance(val, Node):
            val = Node(val)
        self._left_child = val

    @property
    def right_child(self):
        return self._right_child

    def set_right_child(self, val):
        if val and not isinstance(val, Node):
            val = Node(val)
        self._right_child = val

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f'{str(self._data)} left -> {str(self._left_child)} right -> {str(self._right_child)}'


class BinaryTree:
    def __init__(self, root=None):
        if root:
            self._root = root
        else:
            self._root = Node()

    def add_item(self, item):
        if self._root is None:
            self._root = Node(item)
        curr = None
        queue = LinkedList()
        queue.append(self._root)
        while len(queue) != 0:
            curr = queue.remove_first()
            if curr.left_child is None or curr.right_child is None:
                break
            if curr.left_child is not None:
                queue.append(curr.left_child)
            if curr.right_child is not None:
                queue.append(curr.right_child)
        if curr.left_child is None:
            curr.set_left_child(item)
            return
        if curr.right_child is None:
            curr.set_right_child(item)
            return

    def inorder_items(self):
        data = []
        self._inorder_items(self._root, data)
        return data

    def _inorder_items(self, node, items):
        if not node.left_child and not node.right_child:
            items.append(node.data)
            return
        if node.left_child is not None:
            self._inorder_items(node.left_child, items)
        items.append(node.data)
        if node.right_child is not None:
            self._inorder_items(node.right_child, items)

    def level_order_items(self):
        data = []
        queue = LinkedList()
        queue.append(self._root)
        while len(queue) != 0:
            curr = queue.remove_first()
            if curr is None:
                continue
            data.append(curr.data)
            if curr.left_child is not None:
                queue.append(curr.left_child)
            if curr.right_child is not None:
                queue.append(curr.right_child)
        return data

    def remove(self, item):
        if self._root is None:
            return
        deepest_node = None
        delete_node = None
        queue = LinkedList()
        queue.append(self._root)
        while len(queue) != 0:
            curr = queue.remove_first()
            if curr is None:
                continue
            if curr.data == item:
                delete_node = curr
            if curr.left_child is None and curr.right_child is None:
                deepest_node = curr
            if curr.left_child is not None:
                queue.append(curr.left_child)
            if curr.right_child is not None:
                queue.append(curr.right_child)
        if delete_node is not None:
            delete_node.set_data(deepest_node.data)
            self._remove_sub_tree(deepest_node)

    def _remove_sub_tree(self, delete_node):
        if delete_node is None:
            return
        queue = LinkedList()
        queue.append(self._root)
        while len(queue) != 0:
            curr = queue.remove_first()
            if curr is None:
                continue
            if curr.left_child is not None:
                if curr.left_child is delete_node:
                    curr.set_left_child(None)
                else:
                    queue.append(curr.left_child)
            if curr.right_child is not None:
                if curr.right_child is delete_node:
                    curr.set_right_child(None)
                else:
                    queue.append(curr.right_child)

    def height(self):
        return self._height(self._root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left_child)
        right_height = self._height(node.right_child)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
