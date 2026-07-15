class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)       
        elem = 0

        for i in range(k):                 # k * logN
            elem = heapq.heappop(heap)

        return -elem

"""
1)Nlogk  (n inserts to heap of size k)

2) use max-heap  (then we heapify + k extract max = N + klogN) (this one used here)

3) sort then return k largest (NlogN)
"""