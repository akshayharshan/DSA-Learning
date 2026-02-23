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

def rotation_tree(root):
    if not root:
        return None
    root.right,root.left = root.left,root.right
    rotation_tree(root.left)
    rotation_tree(root.right)
    return root


print(rotation_tree(A))