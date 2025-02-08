class BinarySearchTreeNode:
    def __init__(self, key=None):
        self.p = None
        self.left = None
        self.right = None
        if key is not None:
            assert isinstance(key, int), 'keys should be initialized as int'
        self.key = key

    def set_right(self, right):
        assert isinstance(right, BinarySearchTreeNode), 'incorrect input type'
        self.right = right
        right.p = self

    def set_left(self, left):
        assert isinstance(left, BinarySearchTreeNode), 'incorrect input type'
        self.left = left
        left.p = self

    def is_none(self):
        if self.key is None:
            return True
        return False

    def set_key(self, key):
        assert isinstance(key, int), 'keys should be of type int'
        self.key = key


class BinarySearchTrees:
    def __init__(self):
        self.root = BinarySearchTreeNode()

    def insert(self, key):
        if self.root.is_none():
            self.root.set_key(key)
            return True
        new_node = BinarySearchTreeNode(key)
        x = self.root
        while True:
            y = x
            x = x.left if key < x.key else x.right
            if not x:
                if key < y.key:
                    y.set_left(new_node)
                    return True
                y.set_right(new_node)
                return True


def inorder_tree_walk(x):
    if not x: return
    inorder_tree_walk(x.left)
    print(x.key)
    inorder_tree_walk(x.right)

def preorder_tree_walk(x):
    if not x: return
    print(x.key)
    preorder_tree_walk(x.left)
    preorder_tree_walk(x.right)

def postorder_tree_walk(x):
    if not x: return
    postorder_tree_walk(x.left)
    postorder_tree_walk(x.right)
    print(x.key)

def tree_search(x, key):
    if not x:
        return None
    if key == x.key:
        return x
    if key < x.key:
        return tree_search(x.left, key)
    else:
        return tree_search(x.right, key)

def tree_search_iterative(x, key):
    while True:
        if not x:
            return None
        if key == x.key:
            return x
        if key < x.key:
            x = x.left
        else:
            x = x.right

def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x

def tree_minimum_recursive(x):
    if x.left is None:
        return x
    else:
        return tree_minimum_recursive(x.left)

def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x

def tree_maximum_recursive(x):
    if x.right is None:
        return x
    else:
        return tree_maximum_recursive(x.right)

def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while True:
        if not y:
            return y
        if x is not y.right:
            return y
        x = y
        y = y.p

def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.p
    while True:
        if not y:
            return y
        if x is not y.left:
            return y
        x = y
        y = y.p

def inorder_tree_walk_alt(x):
    node = tree_minimum(x)
    res = [node.key]
    while True:
        node = tree_successor(node)
        if not node:
            return res
        res.append(node.key)
