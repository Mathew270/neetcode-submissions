class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        deltas = [[1,0], [0,1], [-1,0], [0,-1]]

        max_size = 0  # max size of dfs

        def dfs(x, y):
            if x >= rows or y >= cols or y < 0 or x < 0 or grid[x][y] == 0 or visited[x][y]:
                return 0
                
            visited[x][y] = True
            size = 1
            for dx, dy in deltas:
                n_row, n_col = x + dx, y + dy
                size += dfs(n_row, n_col)
            
            return size
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_size = max(max_size, dfs(i,j))

        return max_size