class TreeNode:
    def __init__(self,node,left=None,right=None):
        self.left = left
        self.right = right
        self.val = node
    def __str__(self):
        return str(self.val)
    

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(5)
E = TreeNode(7)

A.left = B
A.right = C
C.right = D
C.left = E

# print(A)

from collections import deque
def level_order(node):
    q = deque()
    q.append(node)
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:q.append(node.left)
        if node.right:q.append(node.right)


level_order(A)




        