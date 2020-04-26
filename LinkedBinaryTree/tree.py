class Tree:
    root = None
    size = 0

    def __init__(self, node):
        self.root = node

    def isEmpty(self):
        if (self.root == None and self.size == 0):
            return True
        return False

    def isInternal(self, node):
        if(node.hasChildren()):
            return True
        return False

    def isExternal(self, node):
        if(node.hasChildren()):
            return False
        return True

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