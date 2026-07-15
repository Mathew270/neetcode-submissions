class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # avoid duplicate triplet (repeat of 1st number)

            l, r = i + 1, len(nums) - 1

            while(l < r):
                threesum = nums[i] + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1  # move onto next pair 
                    r -= 1  # has to be incremented also or else we will get same triplet
                    while(l < r and nums[l] == nums[l-1]):
                        l += 1     # to avoid dubplicate triplet (repeat of 2nd number)
        return res