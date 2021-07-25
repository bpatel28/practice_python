from concepts.graph import Graph, Node


graph = Graph()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.children.append(node2)
node1.children.append(node3)
node2.children.append(node1)
node2.children.append(node4)
node3.children.append(node5)
node3.children.append(node6)

nodes = [node1, node2, node3, node4, node5, node6]

graph.nodes = nodes

for node in graph.nodes:
    graph.dfs(node)

print()

for node in graph.nodes:
    graph.bfs(node)
