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
            length += 1       # find length of list
            curr = curr.next

        k = (length - n + 1)  # find position of node from start
        if k == 1:
            return head.next

        i = 1
        curr = head # re-initialize curr to head
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

'''
1) find position of node to be deleted  (from start)

2) go to node before that, save it
    go to node to be deleted, and set the prev node to curr.next

special case (if position == 1)
    then theres no node before it, for above step 2 to work
    if this case just set head to head.next (simple !)
'''

