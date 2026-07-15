class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def back(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            if s[i] == t[j]:
                dp[(i,j)] = back(i + 1, j + 1) + back(i + 1, j)
            
            else:
                dp[(i, j)] = back(i + 1, j)
            
            return dp[(i, j)]
        
        return back(0,0)
            