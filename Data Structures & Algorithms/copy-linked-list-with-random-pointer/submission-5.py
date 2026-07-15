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
        # By initializing the dictionary with {None: None}, 
        # we ensure that any pointer pointing to null in the 
        # original list correctly maps to null in the new list.

        curr = head

        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]

'''
MAIN TAKEAWAY: using nodes as keys and values in hashmaps 
                (to create mapping bw old and new)

easier understood solution is soln 2
essentially its a 2 pass algorithm

1st pass -> map old nodes to new nodes

2nd pass -> use the mapping and assign .next and .random between newly created nodes
'''