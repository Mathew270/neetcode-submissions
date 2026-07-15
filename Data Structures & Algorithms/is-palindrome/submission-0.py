class Solution:
    def isPalindrome(self, s: str) -> bool:
        hashh = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','0'}
        lower = s.lower()
        l = 0
        r = len(s) - 1

        while (l < r):
            while lower[l] not in hashh and l < r:
                l += 1
            while lower[r] not in hashh and l < r:
                r -= 1    
            if lower[l] != lower[r]:
                return False
            l += 1
            r -= 1
        return True

"""
only thing to make sure here is to add the l < r check in both inner 
while loops because it could go out of bounds in the inner while loops

we do the same check even in the 2 way in place partioning algorithm 
in quick sort
"""
        