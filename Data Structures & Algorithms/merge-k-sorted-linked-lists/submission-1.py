# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):    
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                
                else:
                    curr.next = l1
                    l1 = l1.next

                curr = curr.next
            
            curr.next = l1 or l2

            return dummy.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(merge(l1, l2))
            lists = mergedList

        return lists[0]

"""
this qn is basically merge sort but with linkedlists

merge each pair
append the new merged head to mergedlists[]
update lists to be mergedlists[]

stop when len(lists) = 1

A confusion about this qn was on how to merge pairs
store the head of new merged stuff
repeat the merging loop for the newly merged stuff

this was done by creating a temp array called mergedlists[]
an updating lists to mergedlists[] before next iteration
"""


        