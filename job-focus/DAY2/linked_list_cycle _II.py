class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)

# Create nodes
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

# Link them
A.next = B
B.next = C
C.next = D
D.next = E
E.next = C   # Cycle here (starts at 3)

head = A

def linked_list_cycle_II(head):

    slow = head
    fast= head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next 
        
        if fast == slow:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow



    return None





print(linked_list_cycle_II(head))