import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for c in tasks:
            count[c] = count.get(c, 0) + 1

        maxheap = []

        for c in count:
            maxheap.append(-count[c])

        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time += 1

            if maxheap:
                count = heapq.heappop(maxheap)
                count = -count

                if count > 1:
                    q.append((time + n, count - 1))

            if q and q[0][0] == time:
                task = q.popleft()
                heapq.heappush(maxheap, -task[1])

        return time


