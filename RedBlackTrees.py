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
        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else: # elif x is x.p.right:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
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

    def rb_insert(self, key):
        if self.root.is_none():
            self.root.set_key(key)
            return True
        new_node = RedBlackTreeNode(key)
        x = self.root
        while True:
            y = x
            x = x.left if key < x.key else x.right
            if x is self.NIL:
                new_node.p = y
                if key < y.key: y.left = new_node
                else: y.right = new_node
                new_node.left = self.NIL
                new_node.right = self.NIL
                new_node.set_color_red()
                self.rb_insert_fixup(new_node)
                break

    def rb_insert_fixup(self, node):
        while node.p.is_color_red():
            if node.p is node.p.p.left:
                y = node.p.p.right
                if y.is_color_red():
                    node.p.set_color_black()
                    y.set_color_black()
                    node.p.p.set_color_red()
                    node = node.p.p
                else: # elif y.is_color_black()
                    if node is node.p.right:
                        node = node.p
                        self.left_rotate(node)
                    node.p.set_color_black()
                    node.p.p.set_color_red()
                    self.right_rotate(node.p.p)
            else: # elif node.p is node.p.p.right:
                y = node.p.p.left
                if y.is_color_red():
                    node.p.set_color_black()
                    y.set_color_black()
                    node.p.p.set_color_red()
                    node = node.p.p
                else: # elif y.is_color_black()
                    if node is node.p.left:
                        node = node.p
                        self.right_rotate(node)
                    node.p.set_color_black()
                    node.p.p.set_color_red()
                    self.left_rotate(node.p.p)
        self.root.set_color_black()


