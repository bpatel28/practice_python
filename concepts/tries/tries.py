from collections import deque


class TrieNode:
    def __init__(self, char=None, end_of_word=False):
        self.children = dict()
        if char:
            self.children[char] = TrieNode()
        self.end_of_word = end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def traverse(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            print(current.children, current.end_of_word)
            for child in current.children.values():
                queue.append(child)

    def __contains__(self, item):
        current = self.root
        for i in range(len(item)):
            if item[i] not in current.children:
                return False
            current = current.children[item[i]]
        return current.end_of_word

    def is_sub_str(self, item):
        current = self.root
        for i in range(len(item)):
            if item[i] not in current.children:
                return False
            current = current.children[item[i]]
        return True
