
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





G = Node(7)
H = Node(8)
I = Node(9)
J = Node(10)
K = Node(11)
L = Node(12)



A.next = B
B.next = C
C.next = D
D.next = E
E.next = F


G.next = H
H.next = I
I.next = J
J.next = K
K.next = L



def merge_linked_list(list1,list2):

    dummy = Node(0)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1:
        curr.next = list1
    else:
        curr.next =list2
    return dummy.next










print(merge_linked_list(A,G))