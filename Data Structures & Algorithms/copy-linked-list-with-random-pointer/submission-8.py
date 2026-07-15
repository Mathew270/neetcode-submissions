"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # edge case
        if not head:
            return head

        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            new_curr = old_to_new[curr]

            if curr.next:
                new_curr.next = old_to_new[curr.next]
            else:
                new_curr.next = None

            if curr.random:
                new_curr.random = old_to_new[curr.random]
            else:
                new_curr.random = None

            curr = curr.next

        return old_to_new[head]