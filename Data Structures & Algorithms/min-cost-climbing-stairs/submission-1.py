class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        last = cost[-1]
        last2 = cost[n-2]
        cur = 0

        cost0 = 55
        cost1 = 55

        if n <= 2:
            return min(cost[0], cost[1])

        if n == 3:
            return min(cost[0] + cost[-1], cost[1])

        for i in range(n-3, -1, -1):
            cur = cost[i] + min(last2, last)
            last2, last = cur, last2
            if i == 1:
                cost1 = cur
            if i == 0:
                cost0 = cur
        
        return min(cost0, cost1)