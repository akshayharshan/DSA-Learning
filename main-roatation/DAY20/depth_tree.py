class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
A = Node(10)
C = Node(9)
D = Node(11)
E = Node(13)
F = Node(14)

A.left = C
A.right = D
D.left = E
D.right = F

def depth_tree(root):
    height = 0
    if not root:
        return 0
    left = depth_tree(root.left)
    right = depth_tree(root.right)

    height = 1+ max(left,right)
    return height



print(depth_tree(A))