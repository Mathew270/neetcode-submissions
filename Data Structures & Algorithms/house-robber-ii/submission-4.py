class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return max(nums)

        # from 0 to n-2  (not including last)
        cost_prev2 = nums[0]
        cost_prev = max(nums[1], nums[0])
        cost_cur = 0

        for cur in range(2, n-1):   # till 2nd last
            cost_cur = max(cost_prev, nums[cur] + cost_prev2)
            cost_prev, cost_prev2 = cost_cur, cost_prev

        cost_prev2 = nums[1]
        cost_prev = max(nums[2], nums[1])
        cost_cur2 = 0

        for cur in range(3, n):    # till last
            cost_cur2 = max(cost_prev, nums[cur] + cost_prev2)
            cost_prev, cost_prev2 = cost_cur2, cost_prev

        return max(cost_cur, cost_cur2)
