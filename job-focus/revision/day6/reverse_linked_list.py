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


def reverse_linked_list(node):
    prev_node = None
    curr = node
    while curr:
        temp = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = temp
    return prev_node

print(reverse_linked_list(node1))
        


