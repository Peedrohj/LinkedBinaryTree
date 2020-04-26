from position.position import Position
from LinkedBinaryTree.tree import Tree

node = Position(1)
print('node: ', node.element)
print('hasCildren: ', node.hasChildren())

tree = Tree()
tree.addRoot(node)
tree.insertLeft(tree.root, 2)
tree.insertRight(tree.root, 3)
tree.insertLeft(tree.root.left, 4)
tree.insertRight(tree.root.left, 5)


print('Tree size: ', tree.size)
print('Root: ', tree.root.element)
print('Left: ', tree.root.left.element)

print('preOrder: ', tree.toStringPreOrder())


