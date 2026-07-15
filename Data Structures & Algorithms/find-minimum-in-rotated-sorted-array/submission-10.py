class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find peak, using binary search
        # divide array into 2 parts
        # binary search on the one that has the array
        if len(nums) < 3:
            return min(nums[0], nums[-1])

        lo, hi = 1, len(nums) - 2
        maxx = max(nums[-1], nums[0])

        while(lo <= hi):
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                maxx = mid
                return nums[maxx + 1]
            
            elif nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]

            else:
                lo = mid + 1
        
        if maxx == nums[-1]:
            return nums[0]
        else:
            return nums[1]
            

