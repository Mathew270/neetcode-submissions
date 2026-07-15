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
            
        old_to_new = {}
        curr = head

        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = old_to_new[curr]

            if curr.next:
                nextt = old_to_new[curr.next]
                new_node.next = nextt
            
            else:
                new_node.next = None

            if curr.random:
                random = old_to_new[curr.random]
                new_node.random = random
            
            else:
                new_node.random = None

            curr = curr.next

        return old_to_new[head]