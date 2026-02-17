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


def depth_tree(node):

    if not node:
        return 0

    left = depth_tree(node.left)
    right = depth_tree(node.right)

    return  max(left,right)+1




print(depth_tree(A))