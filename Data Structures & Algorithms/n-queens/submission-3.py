class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["."] * n for _ in range(n)]   # initialize to no queens at start

        def isSafe(r, c, board):     
        # checking every previous position we visited that could cause putting a 
        # queen in our curr position invalid
        
        # [NOT IN THIS FUNCTION]
        # 0) same row (previous cols) (ensure every row has only 1 queen)
        #       done by for loop in backtrack()  

        # [IN THIS FUNCTION]
        # 1) same col (previous row)  (checks if every col has no prev queens)
        # 2) diagonal to the left
        # 3) diagonal to the right

            row = r - 1
            while row >= 0:                 # check same col, previous rows 
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:      # check top left diagonal from curr position (r,c)
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1         #  check top right diagonal from curr position (r,c)
            while row >= 0 and col < n:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            
            return True

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]    # for each element in board (list == row) call "".join
                res.append(copy)
                return
            
            for c in range(n):           # we call backtrack on each row, each backtrack func check every col
                if isSafe(r, c, board):  # if safe when compared with prev cells on board, then 
                    board[r][c] = "Q"    # put queen on that cell
                    backtrack(r + 1)     # then move onto next row 
                    board[r][c] = "."    # clear cell for trying next cell (r, c+1)

                    # therefore this for loop ensures each row only has 1 queen

        backtrack(0)
        return res

        