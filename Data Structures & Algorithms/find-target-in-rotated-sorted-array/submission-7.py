class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find minimum position (this divides into 2 arrays) (prev qn)

        # 2 cases + 1 edge case

        # 1) nums[0] <= target <= nums[min_idx - 1] (1st sorted half)
        # 2) nums[min_idx] <= target <= nums[-1] (2nd sorted half)
        # 3) 

        min_idx = 0
        l, r = 0, len(nums) - 1

        while(l < r):
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_idx = l
        print(min_idx)

        if min_idx == 0:
            l, r = 0, len(nums) - 1

        elif nums[0] <= target <= nums[min_idx - 1]:
            l, r = 0, min_idx - 1

        else:
            l, r = min_idx, len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
