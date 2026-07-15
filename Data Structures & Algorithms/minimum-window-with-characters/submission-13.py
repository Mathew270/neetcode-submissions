class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        hash_s = {}

        res_len = float("inf")
        start, end = 1,0
        l = 0

        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1

        def check():
            for c in hash_t:
                if c not in hash_s:
                    return False
                if hash_s[c] < hash_t[c]:
                    return False

            return True

        for r in range(len(s)):
            hash_s[s[r]] = hash_s.get(s[r], 0) + 1

            while(check()):
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    start, end = l, r
                
                hash_s[s[l]] -= 1
                l += 1

        return s[start: end + 1]
"""
These kind of problems are easy when you strictly follow 
the sliding window template,

add element to the window (nums[right] or char[right])
adjust the window till the condition is met(left++)
extend it (right++)

if you try to solve it from first principles, 
then you might miss out some of the corners
"""