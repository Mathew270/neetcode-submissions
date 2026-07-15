class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        n = len(s)
        sett = set(wordDict)

        def solve(i):
            if i == n:
                return True

            if i in dp:
                return dp[i]

            for w in sett:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = solve(i + len(w))

                    if dp[i]:
                        return True
            
            dp[i] = False
            return False
            

        return solve(0)