# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def findTotal(head):
            i = 0
            total = 0
            curr = head

            while curr:
                total += curr.val * (10 ** i)
                i += 1
                curr = curr.next

            return total

        l1_sum = findTotal(l1)
        l2_sum = findTotal(l2)

        sum = (l1_sum + l2_sum)
        string = str(sum)

        dummy = curr = ListNode()

        for digit in string[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next


        