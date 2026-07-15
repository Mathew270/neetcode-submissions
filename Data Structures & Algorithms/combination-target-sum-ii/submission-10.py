class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # now each number in nums[] can only be chosen at most once
        # not infinite like "Combination Sum I"

        res, stack = [], []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(stack[:])
                return

            if i >= len(candidates) or total > target:
                return

            stack.append(candidates[i])
            backtrack(i + 1, total + candidates[i])  # use once
            stack.pop()

            while(i + 1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1
            backtrack(i + 1, total)     # do not use

        backtrack(0,0)

        return res