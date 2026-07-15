class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}  # store coords, length = (x, y, length)
        rows, cols = len(matrix), len(matrix[0])
        max_len = 0

        def dfs(x, y, prev):

            if (x, y, prev) in dp:
                return dp[(x, y, prev)]
            
            if x >= rows or y >= cols or x < 0 or y < 0 or matrix[x][y] <= prev:
                return 0

            curr = matrix[x][y]
            res = 1 + max(dfs(x + 1, y, curr), dfs(x - 1, y, curr), dfs(x, y - 1, curr), dfs(x, y + 1, curr))

            dp[(x, y, prev)] = res

            return res

        for i in range(rows):
            for j in range(cols):
                max_len =  max(max_len,dfs(i, j, -1))

        return max_len