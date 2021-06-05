"""
Given a  directed graph, design an algorithm to find out weather there is a route between two noes.

1 -> 2, 7, 9, 3, 5
2 -> 7
3 -> 9
8 -> 9
5 -> 9
"""
from collections import deque
from enum import Enum


class State(Enum):
    Unvisited = 0
    Visiting = 1
    Visited = 2


class Node:
    def __init__(self, data, children=[], state=State.Unvisited):
        self.data = data
        self.state = state
        self.children = children


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def is_route_exists(self, start, end):
        if start == end:
            return True

        for item in self.nodes:
            item.state = State.Unvisited

        queue = deque()
        queue.append(start)

        while len(queue) != 0:
            node = queue.popleft()
            if node and node.state == State.Unvisited:
                node.state = State.Visited
                if node == end:
                    return True
                for n in node.children:
                    if n.state == State.Unvisited:
                        queue.append(n)
        return False


def __main__():
    node7 = Node(7)
    node9 = Node(9, [node7])
    node2 = Node(2, [node7])
    node3 = Node(3, [node9])
    node8 = Node(8,[node9])
    node5 = Node(5, [node9])
    node1 = Node(1, [node2, node3, node8, node5])
    graph = Graph(node1.children)
    print(graph.is_route_exists(node2, node9))


__main__()
