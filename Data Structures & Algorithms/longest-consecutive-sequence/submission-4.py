class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sett = set(nums)

        for num in nums:
            if num - 1 not in sett:
                cur = 1
                while num + 1 in sett:
                    num += 1
                    cur += 1
                
                longest = max(longest, cur)
        
        return longest
                

        # o(N) we only visit each num at most twice
        # for while loop to be O(N). we only have 1 start of a sequence

        # can also solve using union find
"""
        if nums == []:
            return 0

        nums = set(nums)
        par = {}
        rank = {}

        for i in nums:
            rank[i] = 1
            par[i] = i

        def find(num):
            root = num
            while par[root] != root:
                root = par[root]
            
            while par[num] != num:      # path compression
                temp = par[num]
                par[num] = root
                num = temp

            return root

        def union(num1, num2):
            if rank[num2] > rank[num1]:
                union(num2, num1)      # num1 always greater than num2
            
            else:
                root1 = find(num1)
                root2 = find(num2)

                par[root2] = root1            # update parent
                rank[root1] += rank[root2]    # update rank (size)
        
        for i in nums:
            if i + 1 in nums:
                print(rank[i], rank[i+1])
                union(i, i+1)
                print(rank[i], rank[i+1])
                print(rank[find(i)])
        
        return max(rank.values())
"""
        