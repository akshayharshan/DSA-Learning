class Node:
    def __init__(self,val,next=None):
        
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next = B
B.next = C
C.next = D


def reverse_linked(head):

    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr 
        curr = temp
        
        
    return prev

print(reverse_linked(A))
