class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum position (this divides into 2 arrays) (prev qn)

        # 2 cases

        # 1) nums[min_idx] <= target <= nums[-1] (2nd sorted half)
        # 2) nums[0] <= target <= nums[min_idx - 1] (1st sorted half)

        # the reason we check the first case is because if min_idx is 0 
        # then we get access error if we check 2nd case (nums[min_idx - 1])

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
            
        else:   # target is in 1st sorted half
            l, r = 0, min_idx - 1

        while(l <= r):
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1   # if num was never in array
