class BinarySearchTreeNode:
    def __init__(self, key=None):
        self.p = None
        self.key = key
        self.left = None
        self.right = None
        

class BinarySearchTrees:
    def __init__(self):
        self.root = BinarySearchTreeNode()

    def inorder_tree_walk(self, x):
        if not x: return
        self.inorder_tree_walk(x.left)
        print(x.key)
        self.inorder_tree_walk(x.right)

