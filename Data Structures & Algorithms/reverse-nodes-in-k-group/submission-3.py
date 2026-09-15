# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        curr = head
        while curr.next:
            curr = curr.next
            count += 1
        if count < k:
            return head
        mid = curr = head
        for i in range(count // k):
            tmp = curr
            prev =  None
            for j in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            if i == 0:
                head = prev
            mid.next = prev
            mid = tmp
        mid.next = curr if curr else None
            
        return head
