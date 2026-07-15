import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)    # (x1, y1) -> (w, (x2, y2))

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                w = abs(x1 - x2) + abs(y1 - y2)
                adj[(x1, y1)].append([w, (x2, y2)])
                adj[(x2, y2)].append([w, (x1, y1)])

        edge_est = {tuple(point) : float("inf") for point in points}
        visit = set()           
        # where we store after confirming nodes incoming edge (popping from heap)

        def relax(nbr, w):
            if w < edge_est[nbr]:
                edge_est[nbr] = w
                heapq.heappush(heap, [edge_est[nbr], nbr])
        
        heap = [(0, tuple(points[0]))]

        res = 0
        while len(visit) < len(points):
            inc_edge, point = heapq.heappop(heap)

            if point in visit:
                continue
            res += inc_edge    
            #dont update res as soon as u pop, make sure its not in visited before doing anything
            visit.add(point)

            for w, nbr in adj[point]:
                relax(nbr, w)

        return res
"""
prims algo

n^2logn 

can use indicies to refer to points rather than (x,y) point themselves

append indicies to heap, use indicies to make adj_list rather than tuple(points[i])

done in leetcode
"""