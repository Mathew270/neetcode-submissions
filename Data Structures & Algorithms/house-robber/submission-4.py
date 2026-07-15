class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        cost_first = nums[0]
        cost_second = max(nums[0], nums[1])
        cost_cur = 0

        for cur in range(2, len(nums)):
            cost_cur = max(cost_second, nums[cur] + cost_first)
            cost_first, cost_second = cost_second, cost_cur

        return cost_cur