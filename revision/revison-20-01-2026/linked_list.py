class SinglyLinkedList:
    def __init__(self,current=None,next=None):
        self.current = current
        self.next = next

    def __str__(self):
        return str(self.current)
    
Head  = SinglyLinkedList(1)
A = SinglyLinkedList(2)
B = SinglyLinkedList(3)
C = SinglyLinkedList(4)

Head.next = A
A.next = B
B.next = C
# print(A)

# linked list print all values

curr = Head

while curr:
    print(curr)
    curr = curr.next