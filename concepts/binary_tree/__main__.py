from concepts.binary_tree.binary_tree import BinaryTree, Node

root = Node(25)

tree = BinaryTree(root)

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


print(tree.inorder_items(), tree.height())

print(tree.level_order_items(), tree.height())

tree.remove(10)

print(tree.level_order_items(), tree.height())

tree.remove(25)

print(tree.level_order_items(), tree.height())

tree.remove(31)

print(tree.level_order_items(), tree.height())

tree.remove(90)

print(tree.level_order_items(), tree.height())

tree.remove(4)

print(tree.level_order_items(), tree.height())

tree.remove(18)

print(tree.level_order_items(), tree.height())

tree.remove(12)

print(tree.level_order_items(), tree.height())

tree.remove(35)

print(tree.level_order_items(), tree.height())
