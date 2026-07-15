# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        return prev

        '''
        a -> b -> c -> d -> null

        nextt = a.next
        a.next = prev
        prev = curr
        curr = next

        only thing to rem is the usage of prev
        1) setting it to None
        2) it is the final return value
        '''

