class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

A = Node(5)
B = Node(1)
C = Node(4)
D = Node(3)
E = Node(6)

A.left = B
A.right = C
C.left = D
C.right = E

root = A


def depth_tree(root):
    if not root:
        return 0
    depth = 0
    left = depth_tree(root.left)
    right = depth_tree(root.right)
    depth = 1 + max(left,right)
    return depth


print(depth_tree(root))

