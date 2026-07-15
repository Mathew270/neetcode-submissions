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

            # include curr num
            stack.append(candidates[i])
            backtrack(i + 1, total + candidates[i])  # use once
            stack.pop()    # clear stack

            #exclude curr num
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:   
            # case where we exclude current num, so we need to ensure next number isnt same as curr
                i += 1        # stop at the last index = curr num
            backtrack(i + 1, total)  # since we do i + 1 here (index of next num diff to curr)

        backtrack(0,0)

        return res

"""
we do not want duplicate combinations
the problem of duplicates combinations arises in a situation for eg.

[1,2,2,7] target = 9

from 2 we choose either include this 2 or exclude it

in the path of include we get an ans [2,7] where we include current 2 and 7

in the path of exclusion we reduce the array to [1,2,7]
but then we get a duplicate ans as [2,7] 
here because we include the 2nd 2 and the 7


the problem arises because in the path of excludng the current 2 
we are still met with another 2 in the array

we need to ensure that we do not include the 2nd 2 in our 
(non including 2 decision branch)

--------------------------------------------------------------------------

to do this we use the same way we exclude duplicates in the qn subset II and 3sum

we sort the array initially 

now in the case of excluding current number:
we increment the pointer till we reach the last occurence of current number

then we call backtrack(i + 1)  # i + 1 not points to next diff number

this way we ensure that our excluding branch will truly exclude any other occurence
of current number
"""