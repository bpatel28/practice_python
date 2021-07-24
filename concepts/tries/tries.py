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

    def remove(self, word):
        if len(word) == 0:
            return
        current = self.root
        node_to_del = None

        for char in word:
            if char not in current.children:
                return
            if current.end_of_word:
                node_to_del = (current, char)
            current = current.children[char]
        if current.end_of_word and len(current.children) == 0:
            if node_to_del:
                del node_to_del[0].children[node_to_del[1]]
            else:
                del self.root.children[word[0]]
        current.end_of_word = False
