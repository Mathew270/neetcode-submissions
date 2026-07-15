class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def back(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            if s[i] == t[j]:
                dp[(i,j)] = back(i + 1, j + 1) + back(i + 1, j)
            
            else:
                dp[(i, j)] = back(i + 1, j)
            
            return dp[(i, j)]
        
        return back(0,0)

"""
did myself so its easy dubs

the relation here is that

if s[i] == t[j]

then we can either use the char at s and move forward with the rest of s and rest of t
back(i + 1, j + 1)

or we dont use the char at s and hence make no progress on t
back(i + 1, j)    (still increment i, we just dont use it so j stays same)


if s[i] != t[j]

then we can only do 
back(i + 1, j)
---------------------------------

base cases are obv:
if we reach end of t return 1
if we reach end of s return 0

we have to order them like this since if we reach
the end of t and s at the same time then we sitll return 1


(evidence of repeated subproblems (in notebook, taken pic))
"""
            