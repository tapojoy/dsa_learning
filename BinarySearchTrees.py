class BinarySearchTreeNode:
    def __init__(self, key=None):
        self.p = None
        self.key = key
        self.left = None
        self.right = None


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
