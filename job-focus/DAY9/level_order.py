from collections import deque



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.left = B
A.right = C
B.left = D

root = A
def level_order(root):
    queue = deque()

    if not root:
        return []

    res = []

    queue.append(root)

    while queue:
        level = []
        n = len(queue)

        for i in range(n):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

    
print(level_order(root))




