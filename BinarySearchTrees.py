class BinarySearchTreeNode:
    def __init__(self, key=None):
        self.p = None
        self.left = None
        self.right = None
        if key is not None:
            assert isinstance(key, int), 'keys should be initialized as int'
        self.key = key

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
                new_node.p = y
                if key < y.key:
                    y.left = new_node
                    return True
                y.right = new_node
                return True

    def insert_recursive(self, x, y, node):
        if x is None:
            if node.key < y.key:
                y.left = node
                y.left.p = y
                return True
            y.right = node
            y.right.p = y
            return True
        elif node.key < x.key:
            return self.insert_recursive(x.left, x, node)
        else:
            return self.insert_recursive(x.right, x, node)

    def insert_recursive_helper(self, key):
        if self.root.is_none():
            self.root.set_key(key)
            return True
        new_node = BinarySearchTreeNode(key)
        x = self.root
        y = x.p
        return self.insert_recursive(x, y, new_node)

    def transplant(self, u, v):
        if v is not None:
            assert isinstance(v, BinarySearchTreeNode), 'incorrect type'
        if u.p is None:
            self.root =  v if v is not None else BinarySearchTreeNode()
        elif u.p.left is u:
            u.p.left = v
        elif u.p.right is u:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def tree_delete_by_successor(self, key):
        node = tree_search(self.root, key)
        if not node: return False
        if node.left is None: self.transplant(node, node.right)
        elif node.right is None: self.transplant(node, node.left)
        else:
            y = tree_minimum(node.right)
            if node is not y.p:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.p = y
            self.transplant(node, y)
            y.left = node.left
            y.left.p = y
        return True

    def tree_delete_by_predecessor(self, key):
        node = tree_search(self.root, key)
        if not node: return False
        if node.left is None: self.transplant(node, node.right)
        elif node.right is None: self.transplant(node, node.left)
        else:
            y = tree_maximum(node.left)
            if node is not y.p:
                self.transplant(y, y.left)
                y.left = node.left
                y.left.p = y
            self.transplant(node, y)
            y.right = node.right
            y.right.p = y
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

