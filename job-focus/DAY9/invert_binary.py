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



def invert_binary_tree(root):

    if not root:
        return None
    
    root.left,root.right = root.right,root.left

    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)

    return root

tree = invert_binary_tree(root)

print(root.left.val)






