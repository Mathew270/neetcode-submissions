class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(i, left):
            if (i, left) in dp:
                return dp[(i, left)]

            if left < 0:
                dp[(i, left)] = False
                return dp[(i, left)]

            if i == len(s):
                dp[(i, left)] = (left == 0)
                return dp[(i, left)]

            if s[i] == "(":
                dp[(i, left)] = dfs(i + 1, left + 1)
                return dp[(i, left)]
                
            if s[i] == ")":
                dp[(i, left)] = dfs(i + 1, left - 1)
                return dp[(i, left)]

            dp[(i, left)] = dfs(i + 1, left) or dfs(i + 1, left - 1) or dfs(i + 1, left + 1)
            return dp[(i, left)]
            
        return dfs(0,0)
