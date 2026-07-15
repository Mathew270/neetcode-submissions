class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(x,y):
            # (out of bounds) or (not O) or (visited)
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != "O" or (x,y) in visit:
                return

            visit.add((x,y))
            board[x][y] = "T"

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)


        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    dfs(i,j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"