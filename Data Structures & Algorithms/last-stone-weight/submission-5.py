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
"""
python doesnt support max heap so negate values then insert

s1 and s2 are negative numbers and since we are maintaining a max heap
we want to insert negative of the absolute difference between them

= s2 - s1  (more negative - less negative) = negative (as s2 < s1)

"Continue the simulation until there is no more than one stone remaining."
so either 1 or 0 stones remaining hence the if statement at the end
"""