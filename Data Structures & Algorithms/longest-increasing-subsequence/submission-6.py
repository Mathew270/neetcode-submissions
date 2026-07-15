class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        maxL = 0

        for i in range(n-1,-1,-1):
            for j in range(n-1, i, -1):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                
        return max(dp)