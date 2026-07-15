class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        first, second = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            first, second = second, max(second, first + nums[i])

        return max(first, second)
