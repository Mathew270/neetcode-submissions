class Solution:
    def trap(self, height: List[int]) -> int:

        pref = [0] * len(height)
        post = [0] * len(height)

        res = 0

        for i in range(1, len(height)):
            pref[i] = max(pref[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            post[i] = max(post[i+1], height[i+1])

        for i in range(len(height)):
            water = min(pref[i], post[i]) - height[i]
            if water > 0:
                res += water
        return res

        