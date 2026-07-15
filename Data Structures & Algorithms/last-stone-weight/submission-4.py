import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-1 * s)
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            s1, s2 = max(s1,s2), min(s1,s2)
            if s1 != s2:
                heapq.heappush(heap, s2 - s1)

        return heap[0] * -1 if heap else 0