class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        deltas = [[1,0], [-1,0], [0,1], [0,-1]]  # down, up, right, left
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(x, y, i):
            if i == len(word):
                return True
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False
            if visited[x][y] or board[x][y] != word[i]:
                return False

            visited[x][y] = True
            for dx, dy in deltas:
                if dfs(x + dx, y + dy, i + 1):
                    return True
            visited[x][y] = False  # backtrack
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
