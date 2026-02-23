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


def diameter_tree(root):

    diameter = 0
    def dfs (root):
        nonlocal diameter

        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter,left + right)

        height = 1 + max(left , right)
        return height

        
    
    dfs(root)
    return diameter

print(diameter_tree(A))