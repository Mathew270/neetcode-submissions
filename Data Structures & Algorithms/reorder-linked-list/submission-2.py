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
            if i == middle:  # we do below operations at i == middle cuz then doesnt matter if odd or even length
                rhead = self.reverse(curr.next)
                curr.next = None    #imp
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


'''
1) find length of list

2) find middle node   
       make sure take math.ceil cuz odd numbers 

3) reverse linked list from middle       (same as easy LC qn before)
        call reverse from middle.next
        also make sure to set middle.next to None (might forget, but i didnt tho)

4) merge 1st half and reversed 2nd half  (same as easy LC qn before)
        starting from 1st half

also if making new functions outside given function, use self
'''