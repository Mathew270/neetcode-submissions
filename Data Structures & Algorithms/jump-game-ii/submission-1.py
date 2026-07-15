import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)- 2, -1, -1):
            max_idx = min(len(nums) - 1, i + nums[i])
            dp[i] = 1 + min(dp[i + 1], dp[max_idx])

        return dp[0]