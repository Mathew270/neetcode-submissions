class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[] for i in range(len(nums)+1)]
        print(freq)
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        for num in count:
            freq[count[num]].append(num)

        for arr in freq[::-1]:
            res += arr
            if len(res) >= k:
                return res