class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use bfs 
        # 1st append all rotten to q
        # start bfs from rotten ones
        # set time to all 

        rows, cols = len(grid), len(grid[0])
        deltas = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        q = deque()
        seen_fresh = False

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    seen_fresh = True
                if grid[i][j] == 2: # rotten
                    q.append((i,j))
                    visit.add((i,j))

        if not seen_fresh:
            return 0
        
        time = -1
        while q:
            for f in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                
                for dx, dy in deltas:
                    nr, nc = r + dx, c + dy

                    if nc < 0 or nr < 0 or nc >= cols or nr >= rows or (nr, nc) in visit or grid[nr][nc] == 0:
                        continue
                    
                    visit.add((nr, nc))
                    q.append((nr, nc))
            
            time += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return time
        

