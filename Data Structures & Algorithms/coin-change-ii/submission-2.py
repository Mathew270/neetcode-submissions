class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def tuff(amt, i):
            if (amt, i) in dp:
                return dp[(amt, i)]

            if amt == 0:
                return 1
            
            if amt < 0 or i < 0:
                return 0

            
            dp[(amt, i)] = tuff(amt - coins[i], i) + tuff(amt, i-1)
            return dp[(amt, i)]

        return tuff(amount, len(coins)-1)