class RedBlackTreeNode(BinarySearchTreeNode):
    def __init__(self, key=None):
        super().__init__(key)
        self.color = None
        self.set_color_black()

    def set_color_black(self):
        self.color = 'black'

    def set_color_red(self):
        self.color = 'red'

    def is_color_black(self):
        if self.color == 'black':
            return True
        return False

    def is_color_red(self):
        if self.color == 'red':
            return True
        return False

