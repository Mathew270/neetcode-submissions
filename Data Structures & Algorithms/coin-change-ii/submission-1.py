class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cols, rows = len(coins), amount
        dp = [[0] * (cols + 1) for i in range(rows + 1)]

        for j in range(len(dp[0])):
            dp[0][j] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i >= coins[j - 1]:
                    dp[i][j] = dp[i - coins[j-1]][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]