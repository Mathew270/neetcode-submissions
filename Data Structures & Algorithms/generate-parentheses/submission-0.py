class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()  
                # need to clear stack after this branch is done
                # so that next branch (backtrack call) 
                # can start with a clear stack

            if closeN < openN: 
                # we can only add closing if there is more open than closing
                # in the stack currently

                # we use if rather than else/ elif because each call must 
                # try to execute both if statements

                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0,0)

        return res