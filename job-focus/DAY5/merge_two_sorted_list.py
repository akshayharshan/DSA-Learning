class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __str__(slef):
        return str(slef.val)

# list 1
A = Node(1)
B = Node(2)
C = Node(4)

A.next = B
B.next = C

# list 2
D = Node(1)
E = Node(3)
F = Node(4)

D.next = E
E.next = F

l1 = A
l2 = D





def merge_sorted_lists(l1,l2):

    dummy = Node(None)
    current = dummy
    p1 = l1
    p2 = l2
    while p1 and p2:
        if p1.val <= p2.val:
            current.next = p1
            p1 = p1.next
        else: 
            current.next = p2
            p2 = p2.next
        current = current.next
    if p1:
        current.next = p1
    else:
        current.next = p2
    return dummy.next









curr = merge_sorted_lists(l1,l2)

print(curr.next)