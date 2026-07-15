class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for i in sett:
            curr = 1
            if (i-1) not in sett:
                while i + 1 in sett:
                    curr += 1
                    i += 1
            longest = max(longest, curr)

        return longest