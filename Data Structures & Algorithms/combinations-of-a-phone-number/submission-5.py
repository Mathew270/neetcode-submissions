class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charr = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        stack, res = [], []

        if digits == "":
            return []

        def backtrack(n):
            if n == len(digits):
                res.append("".join(stack))
                return
            
            for c in charr[digits[n]]:
                stack.append(c)
                backtrack(n+1)
                stack.pop()
        
        backtrack(0)
        return res