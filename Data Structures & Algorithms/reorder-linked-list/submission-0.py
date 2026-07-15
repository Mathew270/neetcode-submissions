class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        middle = math.ceil(length/2)
        i = 1

        rhead = None
        while curr:
            if i == middle:
                rhead = self.reverse(curr.next)
                curr.next = None
                break
            i += 1
            curr = curr.next

        self.merge(head, rhead)
            
    def reverse(self, curr):
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        return prev

    def merge(self, head, rhead):
        dummy = curr = ListNode()
        og = True

        while head and rhead:
            if og:
                curr.next = head
                head = head.next
                og = not og
            
            else:
                curr.next = rhead
                rhead = rhead.next
                og = not og
            
            curr = curr.next
        
        curr.next = head or rhead