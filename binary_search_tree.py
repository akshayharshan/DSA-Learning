class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left  = left
        self.right = right
    def __str__(self):
        return str(self.value)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D= TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#preorder
def pre_order(node):
    if not node:
        return 
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
# pre_order(A)


#inorder
def in_order(node):
    if not node:
        return 
    
    in_order(node.left)
    print(node)
    in_order(node.right)
    
# in_order(A)


#post order
def post_order(node):
    if not node:
        return 
    
    post_order(node.left)
    print(node)
    post_order(node.right)
    
# post_order(A)

# iterative way to pre order traversal
def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right : stk.append(node.right)
        if node.left : stk.append(node.left)
# pre_order(A)


from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()

        print(node)

        if node.left : q.append(node.left)
        if node.right : q.append(node.right)

# level_order(A)

def search(node,target):
    if not node:
        return False
    if node.value == target:
        return True
    return search(node.left,target) or search(node.right,target)

print(search(A, 6))


# BST

def search(node,target):
    if not node:
        return False
    if node.value == target:
        return True
    if node.value < target : return search(node.right,target)
    else: return search(node.left,target)
print(search(A,7))

    


        
