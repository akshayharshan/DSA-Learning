class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

# create nodes
head = Node(10)
second = Node(20)
third = Node(30)

# link nodes
head.next = second
second.next = third

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


print(reverse_linked_list(head))

# reverse
new_head = reverse_linked_list(head)

# print reversed list
curr = new_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")