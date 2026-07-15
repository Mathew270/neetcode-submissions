import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # this problem is basically finding minimax path (rec 10 cs2040s)
        # finding the path from src to dest such that it minimises
        # the max edge along that path
        # multiple ways to solve

        # we will do dijkstra + modified relax 
        # if max(est[u], w) < est[v]:
        #      est[v] = max(est[u], w)  
        # ==(max of (largest incoming edge till src (u), incoming edge to v))

        # create adj list
        adj = defaultdict(list)

        rows, cols = len(grid), len(grid[0])
        deltas = [[0,1], [1,0], [-1,0], [0,-1]]

        for i in range(rows):
            for j in range(cols):
                for dx, dy in deltas:
                    r, c = i + dx, j + dy
                    if r < 0 or c < 0 or r >= rows or c >= cols:
                        continue
                    adj[(i,j)].append((grid[r][c], (r,c)))  # u -> (w, v)

        est = [[float("inf")] * cols for _ in range(rows)]
        est[0][0] = grid[0][0]
        visit = set()

        src = (0, (0,0))  # est 0, coords 0,0

        heap = [src]

        def relax(cur, nbr, w):
            x, y = cur[0], cur[1]
            r, c = nbr[0], nbr[1]
            
            if max(est[x][y], w) < est[r][c]:
                est[r][c] = max(est[x][y], w)
                heapq.heappush(heap, (est[r][c], (r, c)))

        while heap:
            cur_est, cur = heapq.heappop(heap)
            if cur in visit:
                continue
            visit.add(cur)

            for w, nbr in adj[cur]:
                relax(cur, nbr, w)   # u, v, w

        return est[rows-1][cols-1]

