# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = prev = None
        while l1 or l2 or carry:
            if l1 and l2:
                node = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
                l1, l2 = l1.next, l2.next
            elif l1:
                node = ListNode((l1.val+ carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
            elif l2:
                node = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
            else:
                node = ListNode(carry)
                carry = 0
            if prev == None:
                prev = node
                head = prev
            else:
                prev.next = node
                prev = node
        return head

            
