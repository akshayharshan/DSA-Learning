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
E = Node(5)

A.next = B
B.next = C
C.next = D
D.next = E



def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        temp_val = current.next
        current.next = prev
        prev = current
        current = temp_val

    return prev








print(reverse_linked_list(A))