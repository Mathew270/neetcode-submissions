class Solution:
    def numDecodings(self, s: str) -> int:
        # if nums[i] = 0, then dp[i] = 0
        # if nums[i] > 2, then dp[i] = dp[i+1] (can only decode as a num by itself)
        # if nums[i] == 2 and nums[i+1] in "789", dp[i] = dp[i+1]
        # else dp[i] = dp[i+1] + dp[i+2] 
        if s[0] == "0":
                return 0

        if len(s) == 1:
            return 1

        if len(s) == 2:
            if int(s[0]) > 2 or int(s) > 26 or "0" in s:
                return 1
            else:
                return 2

        dp = [1] * (len(s) + 1)

        if s[-1] == "0":
            dp[len(s)-1] = 0
        
        for i in range(len(s)-2,-1,-1):

            if s[i] == "0":
                dp[i] = 0

            elif int(s[i]) > 2:
                dp[i] = dp[i+1]

            else:
                tgt = s[i] + s[i+1]
                num = int(tgt)
                if num > 26:
                    dp[i] = dp[i + 1]
                else:
                    dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
            
