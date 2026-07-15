class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        temp = [float("inf")] * n

        dist[src] = 0
        temp[src] = 0

        adj = {i : [] for i in range(n)}

        for u, v, w in flights:
            adj[u].append((w, v))

        # read from dist
        # update in temp
        # after inner loop, dist = temp[:]

        def relax(u, v, w):
            if dist[u] + w < temp[v]:
                temp[v] = dist[u] + w
                q.append((v))

        visit = set()
        q = deque()
        q.append((src))
        #visit.add(src)

        res = 0
        while q and res < k + 1:
            for i in range(len(q)):
                cur = q.popleft()
                #dist[cur] = est
                #visit.add(cur)
                for w, nbr in adj[cur]:
                    relax(cur, nbr, w)
                    #visit.add(nbr)
            res += 1
            dist = temp[:]

        return dist[dst] if dist[dst] != float("inf") else -1

"""
        for i in range(k + 1):
            for j in range(len(flights)):
                u, v, w = flights[j]
                relax(u, v, w)
            dist = temp[:]
"""     

