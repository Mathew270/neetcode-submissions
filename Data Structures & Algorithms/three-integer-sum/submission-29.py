class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while(l < r):
                summ = nums[l] + nums[r]
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while(nums[l + 1] == nums[l] and l + 1 < r):
                        l += 1
                    l += 1
        
        return res