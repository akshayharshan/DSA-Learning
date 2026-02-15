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

def invertedTree(root):

    if root is None:
        return None
    root.left ,root.right = root.right,root.left
    invertedTree(root.left)
    invertedTree(root.right)
    return root




print(invertedTree(A))






# 🌳 Tree Recursion Cheat Sheet
# 1️⃣ Always Start With Base Case
# if node is None:
#     return ...


# For:

# Depth → return 0

# Invert → return None

# Count problems → return 0

# Base case stops recursion.

# 2️⃣ Every Node Solves Its Own Mini Problem

# A node does NOT know the whole tree.

# It only asks:

# What is my left result?

# What is my right result?

# How do I combine them?

# That’s it.

# 🌳 Maximum Depth Mental Note

# Formula:

# depth(node) = 1 + max(depth(left), depth(right))


# Flow:

# Go deep left

# Go deep right

# Return max + 1

# If node is None → return 0

# 🌳 Invert Binary Tree Mental Note

# At every node:

# Swap children

# Tell left child to invert

# Tell right child to invert

# Return node

# Code skeleton:

# if root is None:
#     return None

# root.left, root.right = root.right, root.left

# invert(root.left)
# invert(root.right)

# return root

# 🧠 Recursion Mental Model (Very Important)

# Think like this:

# Recursion =

# Go Down
# Hit Base Case
# Come Back Up

# It always goes:
# Left subtree completely
# Then Right subtree completely

# Never random.