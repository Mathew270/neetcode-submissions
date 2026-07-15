class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = [False] * len(nums)
        res, stack = [], []

        def backtrack():
            if len(stack) == len(nums):
                res.append(stack[:])

            for i in range(len(nums)):
                if not picked[i]:
                    stack.append(nums[i])
                    picked[i] = True

                    backtrack()
                    
                    stack.pop()
                    picked[i] = False
            
        backtrack()
        return res