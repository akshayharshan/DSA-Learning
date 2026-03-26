from collections import deque
def binary_tree_level_order(root):

    if not root:
        return None
    queue = deque()
    queue.append(root)
    ans = []

    while queue:
        inner = []
        n = len(queue)
        for _ in range(len(n)):
            node = queue.popleft()
            inner.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(inner)
    return ans