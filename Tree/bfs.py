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

from collections import deque
def bfs(root):
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result



print(bfs(root))