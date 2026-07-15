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
        
        curr.next = h1 or h2   #set curr.next to head of the non empty list
        
        return dummy.next

'''
things to note

1) use of dummy node (use when u want to create a new list, 
                        saves the hassle of creating initial node 
                        in the loop)

2) while loop condition is (AND) not (or)
    because when either one is empty, we just set curr.next to remaining one

3) dont forget to update pts in node (basic but remember)
            (curr = curr.next)

4) setting final curr.next to head of non-empty list (the reason why we do step 2)

5) return dummy.next

also note we have 2 ptrs to dummy
  1) curr (to increment throughout loop)
  2) dummy (to return dummy.next (node we need) at the end)
'''
