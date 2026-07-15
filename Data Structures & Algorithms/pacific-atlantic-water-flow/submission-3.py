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

        for j in range(cols):     # loop through cols, rows == 0 or rows-1
            dfs(0, j, pac, heights[0][j])
            dfs(rows-1, j, atl, heights[rows-1][j])

        for i in range(rows):     # loop through rows, cols == 0 or cols-1
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])

        for i in range(rows):     # final nested for loop to see coords in both sets
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])

        return res

"""
This qn requires similar out of the box thinking to surrounded regions (next qn)

1) naive approach is to dfs() from every cell and see if there is anyway to reach
    both pacific and atlantic region 
    (this solution is hard to implement as well)
    and even if done, it has time complexity (m*n)^2  (start new dfs on every cell)
----------------------------------------------------------------------------------------------

2) so the way to approach this problem is to think backwards, rather than 
    cell to ocean, we do ocean to cell

    but not check each and every cell (this would just be same as before)

    but rather our idea is to have 2 sets (1 for each ocean)

    start dfs from the border cells (== starting from ocean) and then
    add a cell to our ocean set (pac/ atl) if the height at cell is >= previous

    this way we are essentially adding a cell to our set only when we know it
    has a way to the ocean

    (* a cell can reach an ocean if theres a decreasing height path from cell
    to ocean) 

    if we are stating from pacific, in our dfs we provide (coords, pacific set, prev)

    we add to set if we are (in bounds), (havent seen before) and (>= prev)

    _____________________________________________________________________________
    since we dont revisit cells that are already in a set, time complexity
    is normal dfs() O(m*n)
    _____________________________________________________________________________
    
    coords in both sets give our final answer (can be reached from both oceans)
    (there is an increasing path from both oceans to that cell)


    can be solved using bfs instead of dfs also, since basic idea of finding path 
    and adding cell to set is same
-----------------------------------------------------------------------------------------------

3) 1st for loop is looping through 1st and last row
   2nd for loop is loooping through 1st and last column
   calling dfs

   tricks learnt:

   1)   to pass in sets() in our dfs call

        this qn we modify the set we are passing to our dfs depending on 
        the ocean we are starting from

    2)  looping through 1st and last col/row  (basic but remember)

        for j in range(cols):       for i in range(rows):
            grid[0][j]                  grid[i][0]
            dfs (0,j)                   dfs(i,0)
"""