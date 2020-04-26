from position.position import Position


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def isEmpty(self):
        if (self.root == None and self.size == 0):
            return True
        return False

    def isInternal(self, node):
        if(node.hasChildren()):
            return True
        return False

    def isExternal(self, node):
        if(not node.hasChildren()):
            return True
        return False

    def isRoot(self, node):
        if(node.element == self.root.element):
            return True
        return False

    def hasLeft(self, node):
        if(node.left != None):
            return True
        return False

    def hasRight(self, node):
        if(node.right != None):
            return True
        return False

    def left(self, node):
        return node.left

    def right(self, node):
        return node.right

    def parent(self, node):
        return node.parent

    def children(self, node):
        return [node.left, node.right]

    def addRoot(self, node):
        self.root = node
        self.size = 1

    def insertLeft(self, node, value):
        newNode = Position(value)
        newNode.parent = node

        node.left = newNode
        self.size += 1

    def insertRight(self, node, value):
        newNode = Position(value)
        newNode.parent = node

        node.right = newNode
        self.size += 1

    def toStringPreOrder(self, *node):
        res = ''

        if(node == ()):
            res += str(self.root.element)
            res += self.toStringPreOrder(self.root.left)
            res += self.toStringPreOrder(self.root.right)

        else:
            node = node[0]
            if(node != None):
                res += str(node.element)
                res += self.toStringPreOrder(node.left)
                res += self.toStringPreOrder(node.right)

        return res

    def toStringPosOrder(self, *node):
        res = ''

        if(node == ()):
            node = self.root

        else:
            node = node[0]

        if(node != None):
            res += self.toStringPosOrder(node.left)
            res += self.toStringPosOrder(node.right)
            res += str(node.element)

        return res
