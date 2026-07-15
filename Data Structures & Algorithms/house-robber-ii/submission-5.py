class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        first, second = nums[0], max(nums[0], nums[1])
        maxx = 0

        for i in range(2, n-1):
            first, second = second, max(second, first + nums[i])

        maxx = second

        ##

        first, second = nums[1], max(nums[1], nums[2])

        for i in range(3, n):
            first, second = second, max(second, first + nums[i])

        maxx = max(maxx, second)

        return maxx