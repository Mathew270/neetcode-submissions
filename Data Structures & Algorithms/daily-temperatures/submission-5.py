class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # default value 0 (if no tmp after is greater)
        stack = []

        for (i, temp) in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                idx, t = stack.pop()
                res[idx] =  (i - idx)
            stack.append((i, temp))

        return res

"""
maintains monotonic decreasing order of stack
sets difference of index in res[] for all the elements in stack whose
tmp is lesser than incoming tmp
"""
