class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] 
        # used to keep track of current string of paranthesis
        # we dont use string here since adding a char is O(n)
        # rather we just append to stack, then when we reach the end (== n)
        # we call "".join on stack to make it a string then append 
        # each solution to res
        res = []

#        backtrack function does not return anything it just updates the global
#        stack and res variables (takes in no. of open, close brackets we can use)

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

        