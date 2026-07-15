class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cost_end = 0            # cost after last index
        cost_last = cost[n-1]   # cost at last index
        
        cost_cur = 0
        min_cost = float("inf")

        if n <= 2:
            return min(cost)

        for cur in range(n-2,-1,-1):   # find cost from 2nd last index onwards
            cost_cur = cost[cur] + min(cost_last, cost_end)
            cost_last, cost_end = cost_cur, cost_last

            if cur == 0 or cur == 1:
                min_cost = min(min_cost, cost_cur)
        
        return min_cost