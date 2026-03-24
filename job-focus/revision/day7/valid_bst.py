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

node2.left = node1
node2.right = node3

# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5

def valid_bst(root):
    def dfs(node,min,max):
        if not node:
            return True
        if node.val <= min or node.val >= max:
            return False
        return dfs(node.left,min,node.val) and dfs(node.right,node.val,max)

    
    return dfs(root,float("-inf"),float("inf"))

val = valid_bst(node2)

print(val)


    
