# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # nth node from end = (size - n + 1) from start

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        k = (length - n + 1)  
        if k == 1:
            return head.next
            
        i = 1
        curr = head # re initialize curr
        special = None

        while curr:
            if i == k - 1:
                special = curr
            
            if i == k:
                special.next = curr.next
                curr.next = None
                break
    
            i += 1
            curr = curr.next

        return head

