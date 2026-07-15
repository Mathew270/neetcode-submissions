class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def back(i, total):
            if (i, total) in dp:
                return dp[(i, total)]

            if total == target and i == len(nums):
                return 1
            
            if i >= len(nums):
                return 0
            
            dp[(i, total)] = back(i + 1, total + nums[i]) + back(i + 1, total - nums[i])
            return dp[(i, total)]

        return back(0,0)