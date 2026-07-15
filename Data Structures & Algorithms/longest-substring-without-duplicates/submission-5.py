class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        size = 0

        for r in range(len(s)):
            char = s[r]
            while char in sett:
                sett.remove(s[l])
                l +=1
            sett.add(char)
            size = max(size, r-l+1)

        return size