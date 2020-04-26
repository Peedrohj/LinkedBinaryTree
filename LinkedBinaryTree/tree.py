class position:
    root = None
    size = 0
    
    def __init__(self, node):
        self.root = node

    def isEmpty(self):
        if (self.root == None and self.size == 0):
            return True
        return False

    
