class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            if len(heap) < k:            # if heap has less than k elements
                heapq.heappush(heap, i)
            else:                        # heap has exactly k elements
                heapq.heappushpop(heap, i)
        
        return heap[0]