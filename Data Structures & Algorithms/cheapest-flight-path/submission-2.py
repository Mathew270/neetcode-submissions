class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        temp = [float("inf")] * n

        dist[src] = 0
        temp[src] = 0

        # read from dist
        # update in temp
        # after inner loop, dist = temp[:]

        def relax(u, v, w):
            if dist[u] + w < temp[v]:
                temp[v] = dist[u] + w

        for i in range(k + 1):
            for j in range(len(flights)):
                u, v, w = flights[j]
                relax(u, v, w)
            dist = temp[:]

        return dist[dst] if dist[dst] != float("inf") else -1