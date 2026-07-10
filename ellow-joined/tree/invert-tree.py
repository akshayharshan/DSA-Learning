class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build the tree
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)


def invert_tree(root):
    if not root:
        return None
    
    root.left,root.right = root.right,root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root
    
invert_tree(root)
