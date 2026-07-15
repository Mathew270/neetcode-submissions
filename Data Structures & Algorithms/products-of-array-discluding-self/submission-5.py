class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pref, post = 1,1

        for i in range(len(nums)):
            output[i] = pref
            pref *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]

        return output
