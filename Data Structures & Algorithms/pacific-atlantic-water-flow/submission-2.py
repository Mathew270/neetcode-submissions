class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(x, y, visit, prevHeight):
            if x < 0 or y < 0 or x >= rows or y >= cols or (x,y) in visit or heights[x][y] < prevHeight:
                return  # dont add to visit

            visit.add((x,y))
            dfs(x + 1, y, visit, heights[x][y])
            dfs(x - 1, y, visit, heights[x][y])
            dfs(x, y + 1, visit, heights[x][y])
            dfs(x, y - 1, visit, heights[x][y])

        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows-1, j, atl, heights[rows-1][j])

        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res