class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        sett = set(wordDict)
        dp = {}  
        # stores bool (whether substring starting at idx i to len(nums))
        # is in dictionary

        def dfs(i):

            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            
            for j in range(i, len(s)):
                if s[i:j+1] in sett and (dp.get(i, False) != True):
                    dp[i] = dfs(j + 1)

            if i not in dp:
                dp[i] = False

            return dp[i]
        
        return dfs(0)
