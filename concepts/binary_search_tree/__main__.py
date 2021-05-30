from concepts.binary_search_tree import BinarySearchTree
from concepts.binary_tree import Node

root = Node(25)

tree = BinarySearchTree()

tree.add_item(25)
tree.add_item(25)
tree.add_item(15)
tree.add_item(50)
tree.add_item(10)
tree.add_item(22)
tree.add_item(35)
tree.add_item(70)
tree.add_item(4)
tree.add_item(12)
tree.add_item(18)
tree.add_item(24)
tree.add_item(31)
tree.add_item(44)
tree.add_item(60)
tree.add_item(90)

print(tree.level_order_items())

tree.remove(50)

print(tree.level_order_items())

print(", ".join(map(lambda item: str(item in tree), tree.level_order_items())))

print(-1 in tree)
