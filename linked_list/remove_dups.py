"""
write a code to remove duplicates from an unsorted linked list.
How would you solve problem if temporary buffer is not allowed.

1->4->6->1->8

[1,4,6,8]
"""


class Node:
    def __init__(self, data, next_elem=None):
        self.data = data
        self.next_elem = next_elem


head = Node(1, Node(2, Node(3, Node(1, Node(2)))))

current = head
while current is not None:
    print(current.data, end=", ")
    current = current.next_elem
print()


def remove_dups(list_head):
    current = list_head
    while current is not None:
        runner = current
        while runner is not None and runner.next_elem is not None:
            if runner.next_elem.data == current.data:
                runner.next_elem = runner.next_elem.next_elem
            runner = runner.next_elem
        current = current.next_elem


remove_dups(head)

current = head
while current is not None:
    print(current.data, end=", ")
    current = current.next_elem
print()
