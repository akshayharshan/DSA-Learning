class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(4)
E = TreeNode(8)

A.left = B
A.right = C
C.right = E


def pre_order(node):
    if not node:
        return
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)