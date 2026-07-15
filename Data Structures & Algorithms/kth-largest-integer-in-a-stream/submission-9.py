import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)             # cannot do heap = heapify(nums)
        self.k = k                      # because .heapify returns none (does it in place)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:           # is less than k push
            heapq.heappush(self.heap, val)
        else:                                 # if == k, push then pop
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
