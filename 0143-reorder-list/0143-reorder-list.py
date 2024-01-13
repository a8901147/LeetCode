# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse second 
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        second = prev
        first = head
        while second:
            first_temp = first.next
            second_temp = second.next
            first.next = second
            second.next = first_temp
            
            first = first_temp
            second = second_temp