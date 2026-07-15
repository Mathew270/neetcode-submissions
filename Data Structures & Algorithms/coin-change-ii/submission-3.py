class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for amt in range(1, amount + 1):
                if amt - c >= 0:
                    dp[amt] += dp[amt - c]

        return dp[amount]

"""
Amt Outer	"How can I reach this total, in any order?"	Permutations (e.g., 1+2, 2+1)
Coin Outer	"Using this coin set, how many ways to reach total?"
"""