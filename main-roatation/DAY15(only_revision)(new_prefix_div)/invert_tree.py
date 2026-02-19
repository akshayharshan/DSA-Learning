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


def invert_tree(root):
    if not root:
        return 0
    root.left,root.right = root.right , root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root




print(invert_tree(A))

print(A.right)
