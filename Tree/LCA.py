def lca(root,p,q):
    curr = root
    while curr:
        if p.val > root.val and q.val > root.val:
            curr = root.right
        elif p.val < root.val and q.val < root.val:
            curr = root.left
        else:
            return curr
        



diamter of the tree(revision)


def diameter_tree(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter

        if not node:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(diameter,left+right)

        return 1 + max(left,right)



    dfs(root)
    return diameter

print(diameter_tree(root))








        
    