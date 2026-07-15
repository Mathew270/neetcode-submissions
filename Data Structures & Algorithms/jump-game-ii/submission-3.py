import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        n = len(nums)

        for i in range(n - 1, -1, -1):
            for j in range(i, min(n, i + nums[i] + 1)):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]