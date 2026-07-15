class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def backtrack(i, total):
            if total == target:
                res.append(stack[:])
                return
            if i >= len(nums) or total > target: # only positive numbers
                return
            
            stack.append(nums[i])
            backtrack(i, total + nums[i])  # nums[i] used and can use again
            stack.pop()

            backtrack(i + 1, total)       # dont use nums[i]

        backtrack(0, 0)

        return res