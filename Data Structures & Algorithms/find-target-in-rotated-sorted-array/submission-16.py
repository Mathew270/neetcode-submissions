class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum position (this divides into 2 arrays) (prev qn)

        # 2 cases

        # 1) nums[min_idx] <= target <= nums[-1] (2nd sorted half)
        # 2) nums[0] <= target <= nums[min_idx - 1] (1st sorted half)

        # the reason we check the first case first is because if min_idx is 0 
        # then for the 2nd case we get 
        #       nums[0] <= target <= nums[min_idx - 1]   (2nd case if statement)
        # ==>   nums[0] <= target <= nums[-1]            (min_idx == 0)
        # ==> 1st case

        # if in the case target is in array and min_idx = 0 (normal situation)
        # if we re order the if cases then
        # we will wrongly assign 
        # l, r = 0, -1
        # binary search wont even happen then we return -1 (which is wrong)

        min_idx = 0
        l, r = 0, len(nums) - 1

        while(l < r):
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_idx = l

        if nums[min_idx] <= target <= nums[len(nums) - 1]: 
            l, r = min_idx, len(nums) - 1

        # target is in 2nd sorted half or 
        # the case where min_idx is 0 and target is anywhere in array
            
        elif nums[0] <= target <= nums[min_idx - 1]:  # can be replaced with "else"
            l, r = 0, min_idx - 1

        # target is in 1st sorted half or 
        # not in array at all (min_idx == 0 and target not in array)

        while(l <= r):
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1   # if num was never in array
