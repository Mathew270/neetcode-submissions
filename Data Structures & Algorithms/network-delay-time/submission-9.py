import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}
        est = [float('inf')] * (n + 1)
        est[k] = 0
        visit = set()

        #create adj
        for u, v, w in times:
            adj[u].append((v, w))

        def relax(u, v, w):
            if est[u] + w < est[v]:
                est[v] = est[u] + w
                heapq.heappush(heap, (est[v], v))

        heap = []
        heap.append((0,k))

        while heap:
            cur_est, u = heapq.heappop(heap)
            if u in visit:     # node is visited only after it is popped off (est is confirmed)
                continue
            visit.add(u)

            for v, w in adj[u]:
                relax(u, v, w)

        if len(visit) == n:
            return max(est[1:])  # un-updated index 0 (since all our nodes are 1 to n)
        else:
            return -1

        
