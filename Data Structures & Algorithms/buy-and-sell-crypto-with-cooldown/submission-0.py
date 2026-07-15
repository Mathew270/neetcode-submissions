class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def back(state, i):
            if (state, i) in dp:
                return dp[(state, i)]

            if i >= len(prices):
                return 0
            
            if state == "buy":
                dp[(state, i)] = max( back("sell", i + 1) - prices[i], back("buy", i + 1))
                return dp[(state, i)]

            else:
                dp[(state, i)] = max( back("buy", i + 2) + prices[i], back("sell", i + 1))
                return dp[(state, i)]

        return back("buy",0)