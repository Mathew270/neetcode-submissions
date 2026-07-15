class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))

        def addroom(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1 or (r,c) in visit:
                return
            q.append((r,c))
            visit.add((r,c))

        
        dist = 0
        while q:
            for i in range(len(q)):  # no. of times == no. of curr elements in q
                r, c = q.popleft()
                grid[r][c] = dist

                addroom(r + 1, c)
                addroom(r, c + 1)
                addroom(r - 1, c)
                addroom(r, c - 1)

            dist += 1


        