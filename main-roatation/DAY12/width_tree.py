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


def diameter_of_binary_tree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter,left+right)

        return 1 + max(left,right)
    
    dfs(root)
    return diameter







