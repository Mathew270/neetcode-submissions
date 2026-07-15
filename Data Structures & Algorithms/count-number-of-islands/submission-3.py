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

# simple dfs and find number of connected components (number of times we run dfs) == count
# O(m * n)

# something to consider if we were to use bfs is to make sure we update visited right after we append to q
# in addition to after we deque. because if we ignore updating visited after adding to Q. its possible we add
# something more than 1 time to the queue, which may lead to incorrect results


"""
Notes on dfs():

we can do 2 types of handling for dfs calls

either we call dfs only if all the conditions are met
(in bounds) and qn requirements

eg.
def dfs(x, y):
            visited[x][y] = True

            for dx, dy in deltas:
                n_row, n_col = x + dx, y + dy

                if n_row < rows and n_col < cols and n_col >= 0 and n_row >= 0 and grid[n_row][n_col] == "1" and not visited[n_row][n_col]:
                    dfs(n_row, n_col)

or

we can call dfs without worrying about conditions because we
handle them in the dfs() function itself rather than before the call

if (out of bounds) or .. or .. :
    return 0 / return / return None (depends on qn)

eg.
def dfs(x,y, word, node):
            # if (out of bounds) or (letter not in Trie) or (alr visited) then return nothing
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] not in node.children or (x,y) in visit:
                return

            ...... (remaining code)
            
            dfs(x + 1, y, word, cur)            
            dfs(x - 1, y, word, cur)
            dfs(x, y + 1, word, cur)
            dfs(x, y - 1, word, cur)

"""
