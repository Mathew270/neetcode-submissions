class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        dp = {}

        def solve(i, summ):
            if (i, summ) in dp:
                return dp[(i, summ)]

            if summ == target:
                dp[(i, summ)] = True
                return True

            if summ > target or i >= len(nums):
                dp[(i, summ)] = False
                return False

            dp[(i, summ)] = solve(i + 1, summ + nums[i]) or solve(i + 1, summ)
            return dp[(i, summ)]

        return solve(0, 0)
            

