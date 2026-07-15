class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = [-num for num in nums]
        heapq.heapify(heap)
        elem = 0

        for i in range(k):
            elem = heapq.heappop(heap)

        return -elem

"""
1) this is Nlogk  (n inserts to heap of size k)

2) use max-heap  (then we heapify + k extract max = N + klogN)

3) sort then return k largest (NlogN)
"""