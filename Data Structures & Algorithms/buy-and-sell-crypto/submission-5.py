"""
O(1) memory solution
keep track of minBuy (min of numbers before the next element in prices[])
find max profit using the result of tracked min buy (prices[i] - minBuy)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
        
    """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        post = [0] * len(prices)
        profit = 0
        for i in range(len(prices)-2,-1,-1):
            post[i] = max(prices[i+1], post[i + 1])

        for i in range(len(prices)):
            profit = max(profit, post[i] - prices[i])
        
        return profit
"""

"""
O(n) memory solution, keeping track of postfix max numbers 
post[i] = max of numbers from i + 1 to last index
NOT i to last index (but can be done this way too)
"""