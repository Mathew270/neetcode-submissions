class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                heapq.heappushpop(heap, i)
        
        return heap[0]