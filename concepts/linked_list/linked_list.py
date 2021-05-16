from concepts.linked_list.linked_list_node import LinkedListNode


class LinkedList:
    def __init__(self, head=None, tail=None):
        if head is not None and type(head) is not LinkedListNode:
            raise TypeError("head must be type of LinkedListNode.")
        if tail is not None and type(tail) is not LinkedListNode:
            raise TypeError("tail must be type of LinkedListNode.")
        if tail is None:
            tail = head
        self._head = head
        self._tail = tail

    @property
    def head(self):
        return self._head

    def set_head(self, val):
        self._head = val
        if self._tail is None:
            self._tail = val

    @property
    def tail(self):
        return self._tail

    def set_tail(self, val):
        self._tail = val

    def append(self, item):
        if type(item) is not LinkedListNode:
            item = LinkedListNode(item)
        if self._tail is None:
            self._head = item
            self._tail = item
        else:
            item.set_prev_node(self._tail)
            self._tail.set_next_node(item)
            self._tail = item

    def append_left(self, item):
        if type(item) is not LinkedListNode:
            item = LinkedListNode(item)
        if self._head is None:
            self._head = item
            self._tail = item
        else:
            item.set_next_node(self._head)
            self._head.set_prev_node(item)
            self._head = item

    def remove(self, item):
        if item is None:
            return
        if type(item) is not LinkedListNode:
            item = LinkedListNode(item)
        curr = self._head
        while curr is not None:
            if curr == item:
                prev_node = curr.prev_node
                next_node = curr.next_node
                if prev_node is not None:
                    prev_node.set_next_node(next_node)
                else:
                    self._head = next_node
                if next_node is not None:
                    next_node.set_prev_node(prev_node)
                else:
                    self._tail = prev_node
                del curr
                break
            curr = curr.next_node

    def remove_first(self):
        if self._head is None:
            return
        if self._head is self._tail:
            del self._head
            self._head = None
            self._tail = None
            return
        self._head = self._head.next_node
        self._head.set_prev_node(None)

    def pop(self):
        if self._tail is None:
            return
        if self._head is self._tail:
            del self._head
            self._head = None
            self._tail = None
            return
        self._tail = self._tail.prev_node
        self._tail.set_next_node(None)

    def __iter__(self):
        self._curr = self._head
        return self

    def __next__(self):
        val = self._curr
        if val is None:
            raise StopIteration()
        self._curr = self._curr.next_node
        return val

    def __len__(self):
        length = 0
        curr = self._head
        while curr is not None:
            length += 1
            curr = curr.next_node
        return length

    def __contains__(self, item):
        curr = self._head
        if type(item) is not LinkedListNode:
            item = LinkedListNode(item)
        while curr is not None:
            if curr == item:
                return True
            curr = curr.next_node
        return False

    def __str__(self):
        return f'[{", ".join(map(lambda item: str(item),self))}]'

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be integer.")
        if index >= 0:
            curr = self._head
            counter = 0
        else:
            curr = self._tail
            counter = -1
        while curr is not None:
            if counter == index:
                return curr.data
            if index >= 0:
                counter += 1
                curr = curr.next_node
            else:
                counter -= 1
                curr = curr.prev_node
        raise IndexError("Item not found at given index.")
