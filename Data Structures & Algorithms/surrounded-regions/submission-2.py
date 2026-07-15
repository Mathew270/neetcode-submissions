class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        #visit = set()
        # no need visit since we only care about O's and any O that is visited is marked as T

        def dfs(x,y):
            # (out of bounds) or (not O) or (visited)
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != "O":
                return

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

"""
rather than finding which O's can be converted to X
we find which O's cannot be converted

those O's are the chain of O's that start from the border
so we traverse the borders and call dfs and mark those O's as T's

then after marking T's, we do another for loop and change the 
unchanged O's to X (since these are the O's that can be converted (surrounded))

then change all T's to O
"""