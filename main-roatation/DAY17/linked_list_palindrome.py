class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(2)
E = Node(1)

A.next = B
B.next = C
C.next = D
D.next = E



# find the middle of the linked list


def is_palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:

        fast = fast.next.next
        slow = slow.next
    if fast:
        slow = slow.next
    current = slow
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    first = head
    second = prev

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    return True
        






print(is_palindrome(A))