class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}

        self.left = Node(0,0)
        self.right = Node(0,0)
        
        # inital config (LRU -> <- MRU)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nextt = node.prev, node.next
        prev.next = nextt
        nextt.prev = prev

    def insert(self, node):
        prev, nextt = self.right.prev, self.right
        prev.next = node
        nextt.prev = node

        node.prev = prev
        node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        val = node.value
        self.remove(node)
        self.insert(node)

        return val

    def put(self, key: int, value: int) -> None:

        if key in self.store:
            self.remove(self.store[key])
        self.store[key] = Node(key, value)
        self.insert(self.store[key])
        
        
        if len(self.store) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.store[lru.key]

# understanding the problem
# for an LRU cache to work we need 2 things
"""
1) update an element to be Most Recently Used (after we use get())
2) remove the element that is Least Recently Used

so we need to keep track of 2 things, while having operations be O(1)

we cannot simply have 2 variables representing LRU and MRU

while we could easily implement it for MRU since after each get just set
MRU = element just used

we cant do the same for LRU cuz, once an LRU is removed, it picks the next in line
hence we need to maintain some sort of order

this is why we use a doubly linked list
left end for LRU 
right end for MRU
"""

# Explaining code
"""
Create a Node class with 
- next, prev pointers (standard)
- as well as (key, value)

Initialize cache
- dictionary to store key -> node pairs
- capacity variable
- left pointer node (points to LRU)
- right pointer node (points to MRU)

set left and right to point to each other (initial config)
we will insert and remove over time
--------------------------------------------------------------------

2 helper functions (updating linkedlist pointers)

insert() 
- add a node to be the MRU in linkedlist
- place the node between (right.prev and right) by
- updating pointers of prev, next
- update pointers of newly placed node

remove()
- remove the LRU node in linkedlist
- remove the node by
- updating pointers of prev, next
---------------------------------------------------------------------

get()

- if not in dictionary return -1
- remove() node from linkedlist
- insert() node to linked list  (updates node to be MRU)
- return value of node


put()

- if key exists, update value in dictionary
- remove() node from linkedlist
- create new_node with new value
- insert() new_node to linkedlist

- if key doesnt exist
- create new_node
- add new entry with new_node to dictionary
- insert() new_node to linkedlist

    - if len(list) > capacity (need to remove LRU)
    - remove left.next from linkedlist
    - delete entry from dictionary
"""
