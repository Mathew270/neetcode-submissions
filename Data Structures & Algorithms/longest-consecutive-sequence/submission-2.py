class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for i in sett:
            curr = 1
            if (i-1) not in sett:     # means num is start of a sequence
                while i + 1 in sett:
                    curr += 1
                    i += 1
            longest = max(longest, curr)

        return longest

        # o(N) we only visit each num at most twice
        # for while loop to be O(N). we only have 1 start of a sequence
        