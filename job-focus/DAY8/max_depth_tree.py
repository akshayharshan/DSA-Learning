class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.left = B
A.right = C
B.left = D

root = A

def max_depth(root):

    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)

    depth = 1 + max(left,right)

    return depth

print(max_depth(root))
