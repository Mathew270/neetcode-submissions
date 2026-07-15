class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)

        def encodings(i):
            if i in dp:
                return dp[i]

            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            res = 0
            # Single digit
            if 1 <= int(s[i]) <= 26:
                res += encodings(i + 1)
            
            # Double digits
            if i + 1 < len(s) and 10 <= int(s[i] + s[i+1]) <= 26:
                res += encodings(i + 2)
                
            dp[i] = res
            return dp[i]

        return encodings(0)
        
             

            