import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
# hrs taken to finish a pile = ceil (piles[i] / k)
# total hrs = sum of( hrs taken to finish (each in piles[] ))

# need to find min k such that it is lesser than h (given hrs to finish task)
# idea: is to use binary search and keep reducing search space to valid k's
# valid means f(k) <= h

# if mid is valid then high = mid     (trying to find lowest soln)
# if mid is not valid low = mid + 1    (gone too low, need to increase k, so can finish within k hrs)

# things to consider:
# h should be atleast len(piles) then only we get a valid solution
# if thats the case: k = max(piles), 
# since u cant eat from another pile in the same hour

        k = max(piles)

        lo, hi = 1, k

        def check(k):   # O(n)
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)

            return total

        while(lo < hi):
            mid = (lo + hi) // 2

            if check(mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return hi






