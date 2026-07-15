class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        post = [0] * len(prices)
        profit = 0
        for i in range(len(prices)-2,-1,-1):
            post[i] = max(prices[i+1], post[i + 1])

        for i in range(len(prices)):
            profit = max(profit, post[i] - prices[i])
        
        return profit