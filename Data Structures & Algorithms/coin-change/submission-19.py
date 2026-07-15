class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # no coins needed to make 0

        for c in coins:
            for amt in range(1, amount + 1):
                if amt - c >= 0:
                    dp[amt] = min(1 + dp[amt - c], dp[amt])

        return dp[amount] if dp[amount] != amount + 1 else -1