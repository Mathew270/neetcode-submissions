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
"""
🔁 Permutations:
Goal: Find all order-sensitive arrangements.

Tree structure:

At each level, you can choose any unused number from the list.

So if there are n numbers, the root node has n branches, the next level has n - 1, and so on.

Branching factor: Decreases, but can be up to n at each level.

Height of tree: n

Total paths: n!

📌 Each decision = "Which unused number do I pick next?"
-------------------------------------------------------------------------
➕ Combinations:
Goal: Find all order-insensitive selections.

Tree structure:

At each element, you have exactly 2 choices: include it or exclude it.

This creates a binary decision tree.

Branching factor: 2

Height of tree: n

Total paths: 2^n

📌 Each decision = "Do I include this number or skip it?"
"""