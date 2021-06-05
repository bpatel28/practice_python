"""
Implement an algorithm to find the kth to last element of a singly linked list.

1->3->5->7->9->0
"""


class Node:
    def __init__(self, data, next_elem=None):
        self.data = data
        self.next_elem = next_elem


data = Node(1, Node(3, Node(5, Node(7, Node(9, Node(0))))))

curr = data
while curr is not None:
    print(curr.data, end=', ')
    curr = curr.next_elem
print()


def get_kth_to_end(head, k):
    runner = head
    for i in range(0, k):
        if runner.next_elem:
            runner = runner.next_elem
    curr = head
    while runner:
        if not runner.next_elem:
            return curr.data
        runner = runner.next_elem
        curr = curr.next_elem
    return None


print(get_kth_to_end(data, 5))

