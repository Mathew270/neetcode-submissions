class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best, curr = float("-inf"), 0

        for n in nums:
            curr += n
            best = max(best, curr)

            if curr < 0:
                curr = 0

        return best