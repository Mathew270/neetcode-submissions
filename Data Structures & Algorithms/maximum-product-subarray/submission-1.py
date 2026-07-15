class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        curMax, curMin = 1,1

        for n in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(curMax, curMin, res)

        return res