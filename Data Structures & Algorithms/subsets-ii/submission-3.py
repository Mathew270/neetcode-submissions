class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, stack = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(stack[:])
                return
            
            # include number
            stack.append(nums[i])
            backtrack(i + 1)  # can use number next to it even if same, since we are including it
            stack.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res