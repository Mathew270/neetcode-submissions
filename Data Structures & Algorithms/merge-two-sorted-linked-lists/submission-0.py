# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        dummy = curr = ListNode()

        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                h1 = h1.next
            
            else:
                curr.next = h2
                h2 = h2.next
            
            curr = curr.next
        
        curr.next = h1 or h2
        
        return dummy.next
