class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Symmetric Tree
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3

root = Node(1)

root.left = Node(2)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)
def isSymmetric(root):

    def isMirror(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return isMirror(left.left,right.right) and isMirror(left.right,right.left)       

    return isMirror(root.left,root.right)

print(isSymmetric(root))
