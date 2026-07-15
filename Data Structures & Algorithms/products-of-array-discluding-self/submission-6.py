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

"""
The way to solve this without using division is to use prefix and postfix
product. so for an idx i we need to know the prefix product (till i -1) and 
post fix product (end to i + 1). then the product of those 2 will give
value at idx i

we aim to do this in place (output array) (output array not counted as extra space)

the 1st loop we set the prefix product, 
so for output[0] = 1 (no element before it) (1 is multiplicative identity)
then we update prefix *= nums[i] so we can update the next index of output[]

2nd loop we multiply the post fix onto our already computed prefix all stored in
our output[]
"""