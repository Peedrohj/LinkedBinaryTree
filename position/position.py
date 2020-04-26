class Position:
    element = ''
    parent = None
    left = None
    right = None
    detph = 0

    def __init__(self, element):
        self.element = element

    def hasChildren(self):
        if (self.left and self.right):
            return True
        return False
