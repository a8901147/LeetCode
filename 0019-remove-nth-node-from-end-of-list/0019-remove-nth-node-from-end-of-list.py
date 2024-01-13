# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        for __ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        nxt = slow.next.next
        slow.next = nxt
        return dummy.next