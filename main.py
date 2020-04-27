from position.position import Position
from LinkedBinaryTree.tree import Tree

tree = Tree()
tree.addRoot(Position(1))

root = tree.root

tree.insertLeft(root, 2)
tree.insertRight(root, 3)
tree.insertLeft(root.left, 4)
tree.insertRight(root.left, 5)
tree.insertLeft(root.right, 6)
tree.insertRight(root.left.right, 7)

print('Is empty: ', tree.isEmpty())
print('Tree size: ', tree.size)
print('Root: ', root.element)
print('Left: ', tree.left(root).element)
print('Children: ', tree.children(root))

print('PreOrder: ', tree.toStringPreOrder())
print('PosOrder: ', tree.toStringPosOrder())

print('depth: ', tree.depth(root.left.left))
