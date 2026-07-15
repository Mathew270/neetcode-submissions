# time = O(n * 2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack, res = [], []   # golabl variables we are updating during backtrack

        def backtrack(n):
            if n == len(nums):
                res.append(stack[:]) 
                # need to return copy of stack (list is in place)
                # O(N)

            else:    # if not using "else" here use "return" in previous if statement
                stack.append(nums[n])
                backtrack(n + 1)
                if stack:
                    stack.pop()

                backtrack(n + 1)
                #if stack:
                #    stack.pop()    
                # this part is wrong because we are not adding anything 
                # to the stack to pop from, (trace code and see)
                # we are using the same stack for all recursive calls
                # so we need to make sure we are resetting correctly and only when needed

        backtrack(0)
        
        return res
