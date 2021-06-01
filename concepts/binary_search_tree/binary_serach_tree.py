from concepts.binary_tree import Node, BinaryTree
from concepts.linked_list import LinkedList


class BinarySearchTree(BinaryTree):

    def add_item(self, item):
        if self._root is None:
            self._root = Node(item)
            return
        self._add_item(self._root, item)

    def _add_item(self, node, item):
        if node is None:
            return Node(item)
        if item < node.data:
            if node.left_child is None:
                node.set_left_child(Node(item))
            else:
                self._add_item(node.left_child, item)
        else:
            if node.right_child is None:
                node.set_right_child(Node(item))
            else:
                self._add_item(node.right_child, item)

    def __contains__(self, item):
        return self._contains(self._root, item)

    def _contains(self, node, item):
        if node is None:
            return False
        if node.data == item:
            return True
        if item < node.data:
            return self._contains(node.left_child, item)
        else:
            return self._contains(node.right_child, item)

    @staticmethod
    def min_value_node(node):
        current = node
        while current and current.left_child is not None:
            current = current.left_child
        return current

    def remove(self, item):
        self._remove(self._root, item)

    def _remove(self, root, item):
        if root is None:
            return root

        if item < root.data:
            root.set_left_child(self._remove(root.left_child, item))
        elif item > root.data:
            root.set_right_child(self._remove(root.right_child, item))
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp
            else:
                temp = self.min_value_node(root.right_child)
                root.set_data(temp.data)
                root.set_right_child(self._remove(root.right_child, temp.data))
        return root
