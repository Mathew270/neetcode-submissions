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

            
