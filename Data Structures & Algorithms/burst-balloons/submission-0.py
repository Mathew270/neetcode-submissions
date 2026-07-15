class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = {}

        def dfs(l ,r):

            if (l, r) in dp:
                return dp[(l, r)]
            
            if l > r:
                return 0    # subarray is of size 0 (so max coins u can get from this is 0) 

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1,  r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]
        
        return dfs(1, len(nums) - 2)