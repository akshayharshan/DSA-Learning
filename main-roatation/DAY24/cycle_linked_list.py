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
F = Node(6)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
# F.next = D


def cycle_linked_list(head):
    slow,fast = head,head
    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True


    return False 




print(cycle_linked_list(A))