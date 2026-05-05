class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Build this tree:
#         10
#        /  \
#       5    15
#      / \     \
#     2   7     20

root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.right = Node(20)


def depth_tree(root):

    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        return 1 + max(left,right)


    print(dfs(root))
depth_tree(root)