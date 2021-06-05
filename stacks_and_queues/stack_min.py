"""
How would you design a stack which, in addition to push and pop, has a function min which returns
the minimum element? Push, pop and min should all operate in O(1) time.
"""

from concepts.linked_list.linked_list import LinkedList
import sys


class MinStack(LinkedList):

    def __init__(self):
        self._min_stack = LinkedList()
        super(MinStack, self).__init__()

    def append(self, item):
        if item is None:
            return
        if item <= self.get_min():
            self._min_stack.append(item)
        super(MinStack, self).append(item)

    def get_min(self):
        if len(self._min_stack) == 0:
            return sys.maxsize
        return self._min_stack[len(self._min_stack) - 1]

    def pop(self):
        last_element = super(MinStack, self).pop()
        if len(self._min_stack) != 0 and last_element == self._min_stack[len(self._min_stack) - 1]:
            self._min_stack.pop()
        return last_element


def __main__():
    stack = MinStack()

    stack.append(5)
    stack.append(4)
    stack.append(8)
    stack.append(1)
    stack.append(0)
    stack.append(8)
    stack.append(9)
    stack.append(-1)

    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")

    stack.pop()
    print(stack, f"Min: {stack.get_min()}")


__main__()

