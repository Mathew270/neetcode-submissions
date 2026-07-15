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

"""
find the ending index of each letter

have a l, r pointer
size to keep track of size

l to iterate through each char, 
r will be the ending index for a particular partition

so we update r if we have to for each char( s[l] )

once l is greater than r, we have reached past the end of a partition
record the size
and update size = 0 for next partition

outer loop is to make sure we dont go beyond the string ;ength
inner loop is to iterate through the chars within a partition (<= r)

O(n) time even if nested loop cuz l is incremented by 1 till we reach end of string
O(m) space m = no. of unique chars, O(1) if only alphabets
"""