class Solution:
    def findMin(self, nums: List[int]) -> int:

        # key intuition
        # if our mid value > right value:
        #          the min value is towards the right
        #          (because usually the right will be greater than mid)
        #           so if right is smaller we know a new increasing order
        #           must have started somewhere on the right 
        #           and it started from the min value we are looking for

        #           so reduce search space to right side
        #           lo = mid + 1

        # if our mid <= right:
        #          our min can be the mid value or any value to the left
        #          the reason it cannot be on the right is because

        l, r = 0, len(nums) - 1

        while (l < r):
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

#-------------------------------------------------------------------------

        # find peak, using binary search
        # divide array into 2 parts
        # binary search on the one that has the array
        """
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
        """
            

