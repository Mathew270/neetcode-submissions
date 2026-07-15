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

"""
rather than starting bfs from every land cell and finding closest treasure/gate

we can use a multi source bfs where we append all the treasure/ gates to the q 1st

then from there do bfs and mark dist for all land cells 
then increment dist after for loop (after all cells of that dist are updated)

template for level by level bfs:

dist = 0
while q:
    for i in range(len(q)):
        cur = q.popleft()
        cur.level = dist

        for nbr of cur:
            if (...):                 |
                q.append(nbr)         |   these 3 lines can be a function like above
                visit.add(nbr)        |
        dist += 1
"""


        