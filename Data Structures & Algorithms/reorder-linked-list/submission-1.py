# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def reverse(head):
            curr = head
            prev = None

            while curr:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
            
            return prev
        
        def merge(head, rhead):
            dummy = curr = ListNode()
            og = True

            while head and rhead:
                if og:
                    curr.next = head
                    head = head.next
                    og = False
                
                else:
                    curr.next = rhead
                    rhead = rhead.next
                    og = True
                
                curr = curr.next  # rem to update curr to the next node (the one we just set above)

            curr.next = head or rhead # rem to point to remaining node

            
        if not head or not head.next:
            return

        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
        
        middle = math.ceil(length/2)
        i = 1
        
        curr = head   # re-initialize curr to head
        rhead = None # placeholder
        while curr:
            if i == middle:
                rhead = reverse(curr.next)
                curr.next = None
            i += 1
            curr = curr.next

        merge(head, rhead)

        
