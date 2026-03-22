class node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __str__(self):
        return str(self.val)
    
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

def linked_list_cycle(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow  == fast:
            return True


    return False

print(linked_list_cycle(node1))