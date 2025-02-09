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


class RedBlackTrees:
    def __init__(self):
        self.NIL = RedBlackTreeNode()
        self.NIL.set_color_black()
        self.root = RedBlackTreeNode()
        self.root.set_color_black()
        self.root.p = self.NIL
        self.root.left = self.NIL
        self.root.right= self.NIL

    def left_rotate(self, x):
        assert isinstance(x, RedBlackTreeNode), 'incorrect input type'
        assert x.right is not self.NIL, 'NIL right child, cannot rotate'
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.p = x
        x.p = y.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else: # elif x is x.p.right:
            x.p.right = y
        y.left = x
        x.p = y

    def rotate_right(self, y):
        assert isinstance(y, RedBlackTreeNode), 'incorrect input type'
        assert y.left is not self.NIL, 'NIL left child, cannot rotate'
        x = y.left
        y.left = x.right
        if x.right is not self.NIL:
            x.right.p = y
        x.p = y.p
        if y.p is self.NIL:
            self.root = x
        elif y is y.p.left:
            y.p.left = x
        else: # elif y is y.p.right:
            y.p.right = x
        x.right = y
        y.p = x

