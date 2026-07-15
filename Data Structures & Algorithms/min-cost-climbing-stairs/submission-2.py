class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) <= 2:
            return min(cost)

        first = 0
        second = 0

        n = len(cost)

        for i in range(2, n):
             first, second = second, min(first + cost[i - 2], second + cost[i - 1])

        return min(first + cost[n - 2], second + cost[n - 1])
