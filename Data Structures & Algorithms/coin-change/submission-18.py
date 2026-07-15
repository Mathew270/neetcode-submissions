class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [[float("inf")] * (len(coins) + 1) for i in range(amount + 1)]

        for i in range(len(coins) + 1):  # 1st row (amt = 0) all values = 0
            dp[0][i] = 0

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i - coins[j-1] >= 0:
                    dp[i][j] = min(1 + dp[i-coins[j-1]][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]

        if (dp[-1][-1] == float("inf")):
            return -1
        else:
            return dp[-1][-1]

        """
        Table
                -------\----\----\---\--\
                  ""  1   5   10  20  50   [coins]

            0     0   0   0   0   0   0  
            1    inf  1   1   1   1   1  
            2    inf  1   1   1   1   1
            .
            .
           [amt]

        """
        
        

        """
        dp = {}

        def cc(amt, i):
            if (amt, i) in dp:
                return dp[(amt, i)]

            elif amt == 0:
                dp[(amt, i)] = 0
    
            elif i >= len(coins) or amt < 0:
                dp[(amt, i)] = float("inf")

            else:
                dp[(amt, i)] = min(1 + cc(amt - coins[i], i), cc(amt, i+1))

            return dp[(amt,i)]

        ans = cc(amount, 0)

        return ans if ans != float("inf") else -1
        """
