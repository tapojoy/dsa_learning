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

