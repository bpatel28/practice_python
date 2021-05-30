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

    def remove(self, item):
        if self._root and self._root.data == item:
            if self._root.right_child:
                delete_node = self._root
                self._root = self._root.right_child
                self._append_left_tree(self._root, delete_node.left_child)
            else:
                self._root = self._root.left_child
        self._remove(self._root, item)

    def _remove(self, node, item):
        if node is None:
            return
        if node.left_child and node.left_child.data == item:
            delete_node = node.left_child
            if delete_node.right_child:
                node.set_left_child(delete_node.right_child)
                left_tree = delete_node.left_child
                self._append_left_tree(node.left_child, left_tree)
            else:
                node.set_left_child(delete_node.left_child)
            return
        elif node.right_child and node.right_child.data == item:
            delete_node = node.right_child
            if delete_node.right_child:
                node.set_right_child(delete_node.right_child)
                left_tree = delete_node.left_child
                self._append_left_tree(node.left_child, left_tree)
            else:
                node.set_right_child(delete_node.left_child)
            return
        if item < node.data:
            self._remove(node.left_child, item)
        else:
            self._remove(node.right_child, item)

    @staticmethod
    def _find_min_value(root):
        pass