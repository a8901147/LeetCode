# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists):
            return None
        while len(lists)>1:
            mergeLists = []
            for i in range(0,len(lists),2):
             
                dummy = ListNode()
                temp = dummy
                while i+1<len(lists) and lists[i] and lists[i+1]:
                    if lists[i].val <= lists[i+1].val:
                        temp.next = lists[i]
                        lists[i] = lists[i].next
                    else:
                        temp.next = lists[i+1]
                        lists[i+1] = lists[i+1].next
                    temp = temp.next
                
                if lists[i]:
                    temp.next=lists[i]
                
                if i+1<len(lists) and lists[i+1]:
                    temp.next=lists[i+1]
              
                mergeLists.append(dummy.next)
            lists = mergeLists
        return lists[0]
    
 