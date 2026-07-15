class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sett = set(nums)
        res, stack = [], []

        def backtrack():
            if len(stack) == len(nums):
                res.append(stack[:])

            for num in sett:
                if num not in stack:
                    stack.append(num)
                    backtrack()
                    stack.pop()
            
        backtrack()
        return res