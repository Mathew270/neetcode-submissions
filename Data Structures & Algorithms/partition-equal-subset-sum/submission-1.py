class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # finding a subset where sum(subset) == sum(nums)/2
        # essentitally 0/1 knapsack (cannot only use a num atmost once)

        dp = {}

        if sum(nums)%2:
            return False

        ans = sum(nums)/2

        def back(i, target):
            if (i, target) in dp:
                return dp[(i, target)]

            if target == 0:
                return True
            
            if i >= len(nums) or target < 0:
                return False

            dp[(i, target)] = back(i + 1, target - nums[i]) or back(i + 1, target)

            return dp[(i, target)]

        return back(0, ans)
            


