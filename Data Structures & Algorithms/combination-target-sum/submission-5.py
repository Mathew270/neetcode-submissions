class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []    # can be passed in function also (as done in solution)

        def backtrack(i, total):
            if total == target:
                res.append(stack[:])
                return
            if i >= len(nums) or total > target: # only positive numbers
                return   # not a solution
            
            stack.append(nums[i])
            backtrack(i, total + nums[i])  # nums[i] used and can use again
            stack.pop()   # clear the stack

            backtrack(i + 1, total)       # dont use nums[i]

        backtrack(0, 0)

        return res

# time = O(2^(t/m))  2 ^ height of tree (we reduce total by atleast min value
# in nums[] each time)
# t = target, m = min value in nums[]
# space = O(t/m) size of res array

"""
dp qn: return how many ways can we sum up to target (each num can be used 
infinite num of times) (unbounded knapsack)

the reason why we cannot use dp or why dp differs from this because we need to 
finish going through each recursive branch completely rather than just use the result

-----------------------------------------------------------------------------
in dp:
1) You use and reuse subresults. E.g., dp[5] can be used in multiple places.
2) Overlapping subproblems are solved only once.
3) No need to remember how you got to dp[5] — just that there are X ways.
----------------------------------------------------------------------------
backtracking:
You can't reuse results from the same sub-target (e.g., 5), because the combinations that lead to it might be different.

You can't say:

“Oh, I've already handled target=5, let me just reuse the result.”

Because:

path = [2, 3] reaching target = 3 might produce different combinations than path = [5] reaching target = 3.

So you must fully explore each path.
"""