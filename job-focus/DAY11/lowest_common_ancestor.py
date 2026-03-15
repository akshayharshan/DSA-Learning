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
p = 3
q = 5

def lowest_common_ancestor(root,p,q):

        if not root:
            return None
        if root.val == p or root.val == q:
                return root
        left=lowest_common_ancestor(root.left,p,q)
        right=lowest_common_ancestor(root.right,p,q)

        if left and right:
              return root
        return left if left else right


result = lowest_common_ancestor(root,p,q)
print(result.val)



# LCA(3)
#  ├─ LCA(5)
#  │   ├─ LCA(6) → 6
#  │   └─ LCA(2) → None
#  │   → return 6
#  │
#  └─ LCA(1)
#      ├─ LCA(0) → None
#      └─ LCA(8) → 8
#      → return 8

# At node 3:
# left = 6
# right = 8
# → return 3