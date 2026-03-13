class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

A = Node(5)
B = Node(1)
C = Node(4)
D = Node(3)
E = Node(6)

A.left = B
A.right = C
C.left = D
C.right = E

root = A

def is_valid_bst(root):

    def is_valid(node,min_val,max_val):
        if not node:
            return True
        if node.val >= max_val or node.val <= min_val:
            return False
        
        return is_valid(node.left,min_val,node.val) and is_valid(node.right,node.val,max_val)

    return is_valid(root,float("-inf"),float("inf"))



print(is_valid_bst(root))








