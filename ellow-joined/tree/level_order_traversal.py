class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build the tree
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)



from collections import deque

def level_order_travesal():
    result = []
    queue = deque([root])
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
