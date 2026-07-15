class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for idx, letter in enumerate(s):
            last[letter] = idx

        l = 0
        r = last[s[0]]
        res = []
        size = 0
        
        while l < len(s):
            r = last[s[l]]
            while l <= r:
                size += 1
                r = max(r, last[s[l]])
                l += 1
            res.append(size)
            size = 0

        return res