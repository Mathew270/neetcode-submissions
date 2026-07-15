class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        deltas = [[1,0], [0,1], [-1,0], [0,-1]]

        max_size = 0  # max size of dfs

        def bfs(x,y):
            q = deque()
            visited[x][y] = True
            q.append((x,y))
            res = 1

            while q:
                r, c = q.popleft()
                for dx, dy in deltas:
                    nr, nc = r + dx, c + dy
                    if (nr < 0 or nc < 0 or nr >= rows or
                        nc >= cols or visited[nr][nc] or grid[nr][nc] == 0
                    ):
                        continue

                    q.append((nr, nc))
                    visited[nr][nc] = True
                    res += 1

            return res
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_size = max(max_size, bfs(i,j))

        return max_size

"""
def dfs(x, y):
            if x >= rows or y >= cols or y < 0 or x < 0 or grid[x][y] == 0 or visited[x][y]:
                return 0               # invalid or out of bounds return 0 (additive identity)

            visited[x][y] = True
            size = 1                   # size of 1 as default (for valid coords)
            for dx, dy in deltas:
                n_row, n_col = x + dx, y + dy
                size += dfs(n_row, n_col)      # increase size by adding with size of nbrs
            
            return size
"""