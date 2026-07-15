class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []    # can be passed in function also (as done in solution)

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

# time = O(2^(t/m))  2 ^ height of tree t = target, m = min value in nums[]
# space = O(t/m) size of res array