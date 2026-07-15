class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack, res = [], []

        def backtrack(n):
            if n == len(nums):
                res.append(stack[:])

            else:
                stack.append(nums[n])
                backtrack(n + 1)
                if stack:
                    stack.pop()

                backtrack(n + 1)

        backtrack(0)
        
        return res