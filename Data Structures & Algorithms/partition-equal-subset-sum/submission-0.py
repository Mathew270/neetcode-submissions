class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # finding a subset where sum(subset) == sum(nums)/2

        if sum(nums)%2:   # remainder == 1, then odd
            return False

        ans = sum(nums)/2
        
        total = [0]

        def back(i):
            
            if total[0] == ans:
                return True

            if i == len(nums):
                return False
            
            num = nums[i]
            total[0] += num
            ans1 = back(i + 1)
            total[0] -= num

            ans2 = back(i + 1)

            return ans1 or ans2
        
        return back(0)

