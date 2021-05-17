class TreeNode:
    def __init__(self, data=None, left_child=None, right_child=None):
        self._data = data
        self._left_child = left_child
        self._right_child = right_child

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def set_left_child(self, val):
        self._left_child = val

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def set_right_child(self, val):
        self._right_child = val
