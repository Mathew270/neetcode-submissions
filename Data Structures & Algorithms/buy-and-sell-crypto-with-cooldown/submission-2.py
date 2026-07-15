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

"""
here the subproblem is:
    max money we can obtain from index i (i at len(prices) == 0)

    so cacheing each indexs result is useful since u will need it
    when u reach that particular index from an earlier index

    since we get the results for the later indicies first

    this way we wont have to recompute the max we can obtain from a certain index
    once we have stored its result

    we dont exactly store "only the max result needed" but rather every previous
    descision/ branch so when we compute

    max (decision 1, decision 2).

    those values will have been already computed
"""
