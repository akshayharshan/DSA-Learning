class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.left = B
A.right = C
B.left = D
B.right = E

root = A



def diameter(root):
    diameter = 0
    def dfs(root):
        nonlocal diameter
        if not root:
            return 0

        left = dfs(root.left) 
        right = dfs(root.right)
        diameter = max(diameter,left + right)
        return 1 + max(left,right)
    dfs(root) 
    return diameter
    
print(diameter(root))