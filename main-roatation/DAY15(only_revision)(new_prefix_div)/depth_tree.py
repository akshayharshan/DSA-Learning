class Node:
    def __init__(self,val,right=None,left=None):
        self.left = left
        self.val = val
        self.right = right

    def __str__(self):
        return str(self.val)
    

A = Node(10)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.left = B
B.left = F
A.right = C
C.right = D
C.left = E


def depth_tree(root):
    height = 0
    if not root:
        return 0

    left = depth_tree(root.left)
    right = depth_tree(root.right)

    height = 1 + max(left,right)

    return height




print(depth_tree(A))
