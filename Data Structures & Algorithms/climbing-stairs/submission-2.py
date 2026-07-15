class Solution:
    def climbStairs(self, n: int) -> int:

        last2 = 1  #(n-1)
        last3 = 2  #(n-2)
        cur = 0

        if n <= 2:
            return n

        for i in range(n-3,-1,-1):
            cur = last2 + last3
            last3, last2 = cur, last3

        return cur

        """
        start from step 0 have to reach step n

        no. of ways to reach step n from step n-1 = 1 (take 1 step)
        no. of ways to reach step n from step n-2 = 1 (take 2 steps) or (take 1 step twice)

        """