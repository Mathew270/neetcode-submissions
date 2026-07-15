class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxx = 1
        answer = s[0]
        b, e = 0, 0    # store beginning, end indicies of longest palindromic substring

        # odd length
        for i in range(1, n):
            l, r = i - 1, i + 1
            curr = 1
            while l >= 0 and r < n and s[l] == s[r]:
                curr += 2
                l -= 1
                r += 1
            
            if curr > maxx:
                maxx = curr
                b, e = l + 1, r - 1

        # even length
        for i in range(n-1):
            l, r = i, i + 1
            curr = 0
            while l >= 0 and r < n and s[l] == s[r]:
                curr += 2
                l -= 1
                r += 1
            
            if curr > maxx:
                maxx = curr
                b, e = l + 1, r - 1

        return s[b:e + 1]

"""
coded this myself

set default length = 1, answer = s[0]

1st find odd length palindromes 
(while in bounds and s[l] == s[r])
add 2 to length

if length is best we found
update maxx
update indicies

then do the same for even length palindromes
"""