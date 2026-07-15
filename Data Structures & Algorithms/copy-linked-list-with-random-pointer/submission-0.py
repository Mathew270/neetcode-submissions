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
        if not head:
            return None

        old_to_new = {None: None}
        curr = head
        dummy = Node(7)
        start = dummy
        begin = dummy

        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            dummy.next = new_node
            curr = curr.next
            dummy = dummy.next

        curr = head
        start = start.next
        
        while curr:
            start.random = old_to_new[curr.random]
            curr = curr.next
            start = start.next

        return begin.next