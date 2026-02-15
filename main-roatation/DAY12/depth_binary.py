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

max_depth = 0
def depth_tree(Node):
    if Node is None:
        return 0
    max_depth = 1+max(depth_tree(Node.left),depth_tree(Node.right))
    return max_depth




print(depth_tree(A))
