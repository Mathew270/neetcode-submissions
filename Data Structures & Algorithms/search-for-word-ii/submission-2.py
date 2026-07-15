class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
    
        def dfs(x, y, word, i, visited):
            if i == len(word):
                return True
            if x >= rows or y >= cols or x < 0 or y < 0 or visited[x][y] or board[x][y] != word[i]:
                return False
            
            visited[x][y] = True

            ans = dfs(x + 1, y, word, i + 1, visited) or dfs(x, y + 1, word, i + 1, visited) or dfs(x - 1, y, word, i + 1, visited) or dfs(x, y - 1, word, i + 1, visited)
            
            visited[x][y] = False

            return ans


        def search(word):
            visited = [[False] * cols for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if dfs(i, j, word, 0, visited):
                        return True
            return False

        output = []
        for word in words:
            if search(word):
                output.append(word)

        return output