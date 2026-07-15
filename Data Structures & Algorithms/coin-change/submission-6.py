class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
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
