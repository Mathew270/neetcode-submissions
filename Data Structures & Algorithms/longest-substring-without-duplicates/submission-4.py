class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            res = max(res, r - l + 1)

        return res

"""
the key to sliding window is to keep increasing 
the window (move right pointer) until the condition fails

then we keep decreasing the window (increment left pointer) until we reach 
a valid window again

then keep track of the property/ do the required operation for every valid
window encountered

then repeat process
"""
        