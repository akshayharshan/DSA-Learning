class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)

# node2.left = node1
# node2.right = node3

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


def diameter_tree(root):
    width = 0
    def dfs(root):
        nonlocal width
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)

        width = max(width , (left + right))
        return 1 + max(left,right)
    dfs(root)
    return width




print(diameter_tree(node1))