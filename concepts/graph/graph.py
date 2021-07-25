from enum import Enum
from  collections import deque


class State(Enum):
    NotVisited = 0
    Visited = 1


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
        self.state = State.NotVisited

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.nodes = []

    def dfs(self, node):
        for n in self.nodes:
            n.state = State.NotVisited
        self._dfs(node)
        print()

    def _dfs(self, node):
        print(node, end=" - ")
        node.state = State.Visited
        for child in node.children:
            if child.state == State.NotVisited:
                self._dfs(child)

    def bfs(self, node):
        for n in self.nodes:
            n.state = State.NotVisited
        q = deque()
        q.append(node)
        while q:
            n = q.popleft()
            print(n, end=" - ")
            n.state = State.Visited
            for child in n.children:
                if child.state == State.NotVisited:
                    q.append(child)
        print()
