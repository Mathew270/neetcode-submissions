class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # find based on the subproblem
        # LIS ending at index i

        dp = [1] * len(nums)
        n = len(nums)

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
