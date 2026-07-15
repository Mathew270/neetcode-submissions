class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        stack, res = [], []

        def backtrack(i):
            if i == len(s):
                res.append(stack[:])
                return
            
            for j in range(i, len(s)):
                if check(i,j):
                    stack.append(s[i:j+1])
                    backtrack(j + 1)

                    stack.pop()
        
        backtrack(0)
        return res

"""
                                aab
                            a   aa    aab    (all possible partitions starting from index 0)
                        ab
                    a  ab 
                b      x

for each index we check for each possible partition starting from that index
i is current index and j is where we boundaary the 1st and 2nd part of partition

if i to j is a palindrome
    we add for s[i:j+1] to stack
    and check for j + 1 (recusively)
    clear stack for after that branch is done (stack.pop())
"""