class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        len = 0
        while curr:
            len +=1
            curr = curr.next
        mid = len//2
        curr = head
        for _ in range(mid):
            curr = curr.next
        return curr