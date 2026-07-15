class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # default value 0 (if no tmp after is greater)
        stack = []

        for i, tmp in enumerate(temperatures):
            while(stack and tmp > stack[-1][1]):
                top = stack.pop()
                res[top[0]] = i - top[0]

            stack.append((i, tmp))
        
        return res

"""
maintains monotonic decreasing order of stack
sets difference of index in res[] for all the elements in stack whose
tmp is lesser than incoming tmp
"""
