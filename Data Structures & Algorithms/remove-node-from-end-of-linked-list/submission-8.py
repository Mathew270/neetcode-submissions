# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
   
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # find position from the start of the node we need to remove
        n = (length - n + 1)
        
        # special case if we need to remove the 1st node
        if n == 1:
            return head.next 
        
        # find node before the node we need to remove, 
        # set curr.next to curr.next.next
        i = 1
        curr = head
        while curr:
            if i == (n-1):
                curr.next = curr.next.next
                break
            i += 1
            curr = curr.next
        return head