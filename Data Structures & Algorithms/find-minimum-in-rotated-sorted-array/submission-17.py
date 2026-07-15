class Solution:
    def findMin(self, nums: List[int]) -> int:

        # key intuition

        # if our mid value > right value:   (special case)
        #          the min value is towards the right
        #          (because usually the right will be greater than mid)
        #           so if right is smaller we know a new increasing order
        #           must have started somewhere on the right 
        #           and it started from the min value we are looking for

        #           so reduce search space to right side
        #           lo = mid + 1

        # if our mid <= right:  (normal case) (situation in regular bin sear)
        #          our min can be the mid value or any value to the left
        #          the reason it cannot be on the right is because
        #          everything on the right will be greater (sorted)

        #          the only time when something on the right is not bigger
        #          is when the min is somewhere on the right
        #          we handle this case in the previous if
        
        l, r = 0, len(nums) - 1

        while (l < r):
            mid = (l + r) // 2   # brackets matter

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]
        
#-------------------------------------------------------------------------

        # we know min element is 1 index to the right of max

        # in our bin search we assume we are deailing with special case where 
        # there is rotation, the normal case we handle separately later

        # we binary search excluding 1st and last element so we dont run into
        # access error during nums[mid - 1] or nums[mid + 1]
        # we will handle the situations where we need to include 
        # 1st and last index later

        # in binary search
        # if we find max, return max + 1
        # if we find min return min
        # else lo = mid + 1   (min will be on the right) (since we assume this is rotated)

        # handle edge cases
        # where there is no rotation
        # since we exitted bin search withour returning that means
        # max is either in index 0 or las index
        # if max is 0, then min is 1
        # if max is last index then min is 0 (normal case: no rotation)
        
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
        
            

