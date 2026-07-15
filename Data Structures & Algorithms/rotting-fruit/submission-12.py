class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use multi source bfs (like walls and gates qn) 
        # 1st append all rotten to q
        # start bfs from rotten ones
        # set each cell from fresh to rotten (1 to 2)

        rows, cols = len(grid), len(grid[0])
        deltas = [[0,1],[1,0],[-1,0],[0,-1]]
        #visit = set()   # no need since we know its not visited if cell == 1
        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2: # rotten
                    q.append((i,j))
        
        time = 0
        while q and fresh > 0:       # stop when q is empty or all fresh is rotten
            for f in range(len(q)):
                r, c = q.popleft()
                
                for dx, dy in deltas:
                    nr, nc = r + dx, c + dy

                    if nc < 0 or nr < 0 or nc >= cols or nr >= rows or grid[nr][nc] != 1:
                        # (out of bounds) or (not fresh)
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1
        

