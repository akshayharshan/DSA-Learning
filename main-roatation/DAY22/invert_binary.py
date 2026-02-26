class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.left = B
A.right = C
B.left = D
B.right = E



def invert_binary(root):

    if not root:
        return None
    root.left,root.right = root.right,root.left
    invert_binary(root.left)
    invert_binary(root.right)
    return root


invert_binary(A)
print(A.left)
