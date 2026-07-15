class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        deltas = [[1,0], [0,1], [-1,0], [0,-1]]


        def dfs(x, y):
            visited[x][y] = True

            for dx, dy in deltas:
                n_row, n_col = x + dx, y + dy

                if n_row < rows and n_col < cols and n_col >= 0 and n_row >= 0 and grid[n_row][n_col] == "1" and not visited[n_row][n_col]:
                    dfs(n_row, n_col)

        count = 0  # no. of times we run dfs

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i,j)
                    count += 1

        return count