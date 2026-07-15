class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def back(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                dp[(i, j)] = back(i + 1, j + 1)

            else:
                dp[(i, j)] = 1 + min(back(i + 1, j), back(i, j + 1), back(i + 1, j + 1))

            return dp[(i, j)]

        return back(0,0)

            