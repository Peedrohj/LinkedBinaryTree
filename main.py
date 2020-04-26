from position.position import Position
from LinkedBinaryTree.tree import Tree

node = Position('1')
print('node: ', node.element)
print('hasCildren: ', node.hasChildren())

tree = Tree(node)
print('Tree: ', tree.size)