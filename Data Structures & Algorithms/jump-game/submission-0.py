class Solution:
    def canJump(self, nums: List[int]) -> bool:
        earliest_true = len(nums) - 1
        can_reach = True

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= earliest_true:
                earliest_true = i
                can_reach = True
            
            else:
                can_reach = False

        return can_reach