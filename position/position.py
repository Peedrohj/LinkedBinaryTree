class Position:
    def __init__(self, element):
        self.element = element
        self.parent = None
        self.left = None
        self.right = None

    def hasChildren(self):
        if (self.left or self.right):
            return True
        return False